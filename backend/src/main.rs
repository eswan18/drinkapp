use axum::Router;
use tower_http::validate_request::ValidateRequestHeaderLayer;
use tokio::net::TcpListener;
pub use self::error::{Error, AppResult};

mod models;
mod error;
mod web;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .merge(web::routes_drink::routes())
        .merge(web::routes_hello::routes())
        // .route("/drink", post(handlers::drink::save_drink))
        .layer(ValidateRequestHeaderLayer::bearer("abc"));
    let listener = TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}