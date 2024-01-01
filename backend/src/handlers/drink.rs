use axum::Json;
use crate::models::drink::Drink;


pub async fn save_drink(Json(payload): Json<Drink>) -> String {
    format!("Received: {:?}", payload)
}