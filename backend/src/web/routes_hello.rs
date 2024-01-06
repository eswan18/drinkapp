use axum::{Router, debug_handler, routing::get};

pub fn routes() -> Router {
    Router::new().route("/drink", get(get_hello))
}

#[debug_handler]
pub async fn get_hello() -> String {
    "hey!".to_string()
}