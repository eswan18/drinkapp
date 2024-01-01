use crate::handlers::hello::get_hello;
use crate::handlers::drink::save_drink;

use axum::{
    Router,
    routing::{get, post},
};

pub fn app_routes() -> Router {
    Router::new()
        .route("/hello", get(get_hello))
        .route("/drink", post(save_drink))
}
