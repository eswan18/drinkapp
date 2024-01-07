use axum::{Json, debug_handler, Router, extract::State};
use axum::routing::{get, post};
use crate::models::Drink;
use crate::{AppResult, AppState};
use serde_json::{json, Value};
use chrono::Utc;
use uuid::Uuid;


pub fn routes() -> Router<AppState> {
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
async fn get_drinks(State(state): State<AppState>) -> AppResult<Json<Value>> {
    let drinks = sqlx::query_as!(Drink, "SELECT user_id, timestamp FROM user_drinks");
    let drink1 = Drink {
        timestamp: Utc::now().naive_utc(),
        user_id: Uuid::new_v4(),
    };
    let drink2 = Drink {
        timestamp: Utc::now().naive_utc(),
        user_id: Uuid::new_v4(),
    };
    let body = Json(json!(vec![drink1, drink2]));
    Ok(body)
}