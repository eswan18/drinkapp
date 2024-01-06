use axum::{Json, debug_handler, Router};
use axum::routing::{get, post};
use crate::models::Drink;
use crate::AppResult;
use serde_json::{json, Value};
use chrono::Utc;
use uuid::Uuid;


pub fn routes() -> Router {
    Router::new()
        .route("/drink", get(get_drinks))
        .route("/drink", post(save_drink))
}

#[debug_handler]
async fn save_drink(Json(_payload): Json<Drink>) -> AppResult<Json<Value>> {
    let body = Json(json!({
        "message": "Drink saved!",
    }));
    Ok(body)
}

#[debug_handler]
async fn get_drinks() -> AppResult<Json<Value>> {
    let drink1 = Drink {
        timestamp: Utc::now(),
        user_id: Uuid::new_v4(),
    };
    let drink2 = Drink {
        timestamp: Utc::now(),
        user_id: Uuid::new_v4(),
    };
    let body = Json(json!(vec![drink1, drink2]));
    Ok(body)
}