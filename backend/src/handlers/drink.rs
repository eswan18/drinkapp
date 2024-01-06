use axum::{Json, debug_handler};
use http::StatusCode;
use crate::models::drink::Drink;
use crate::app_result::AppError;


#[debug_handler]
pub async fn save_drink(Json(payload): Json<Drink>) -> Result<(StatusCode, String), AppError> {
    Ok((StatusCode::OK, format!("Received: {:?}", payload)))
}