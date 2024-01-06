use axum::{Router, routing::{get, post}};
use tower_http::validate_request::ValidateRequestHeaderLayer;
use tokio::net::TcpListener;

mod handlers;
mod models;
mod app_result;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/hello", get(handlers::hello::get_hello))
        .route("/drink", post(handlers::drink::save_drink))
        .layer(ValidateRequestHeaderLayer::bearer("abc"));
    let listener = TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}