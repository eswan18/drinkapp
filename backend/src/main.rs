pub use self::error::{AppResult, Error};
use axum::Router;
use dotenvy::dotenv;
use sqlx::postgres::PgPoolOptions;
use sqlx::{Pool, Postgres};
use tokio::net::TcpListener;
use tower_http::validate_request::ValidateRequestHeaderLayer;

mod error;
mod models;
mod web;

#[derive(Clone)]
struct AppState {
    pub pool: sqlx::PgPool,
}

#[tokio::main]
async fn main() {
    // Load .env file
    dotenv().expect(".env file not found");

    // Set up the db pool.
    let database_url = std::env::var("DATABASE_URL").expect("DATABASE_URL not set");
    let pool: Pool<Postgres> = PgPoolOptions::new()
        .max_connections(5)
        .connect(&database_url)
        .await
        .unwrap();

    let state = AppState { pool };
    let app = Router::new()
        .merge(web::routes_drink::routes())
        .merge(web::routes_hello::routes())
        .layer(ValidateRequestHeaderLayer::bearer("abc"));
    let app = app.with_state(state);
    let listener = TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
