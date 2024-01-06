use axum::{Json, debug_handler, Router};
use axum::routing::post;
use crate::models::Drink;
use crate::AppResult;
use serde_json::{json, Value};


pub fn routes() -> Router {
    Router::new().route("/drink", post(save_drink))
}

#[debug_handler]
pub async fn save_drink(Json(_payload): Json<Drink>) -> AppResult<Json<Value>> {
    let body = Json(json!({
        "message": "Drink saved!",
    }));
    Ok(body)
}