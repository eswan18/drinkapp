use crate::AppState;
use axum::{debug_handler, routing::get, Router};

pub fn routes() -> Router<AppState> {
    Router::new().route("/hello", get(get_hello))
}

#[debug_handler]
pub async fn get_hello() -> String {
    "hey!".to_string()
}
