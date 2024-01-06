use axum::{Json, debug_handler};
use crate::models::drink::Drink;


#[debug_handler]
pub async fn save_drink(Json(payload): Json<Drink>) -> String {
    format!("Received: {:?}", payload)
}