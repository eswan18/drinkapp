use axum::{Json, debug_handler, Router, extract::State};
use axum::routing::{get, post};
use crate::models::Drink;
use crate::{AppResult, AppState, Error};
use serde_json::{json, Value};
use sqlx::postgres::PgQueryResult;


pub fn routes() -> Router<AppState> {
    Router::new()
        .route("/drink", get(get_drinks))
        .route("/drink", post(save_drink))
}

#[debug_handler]
async fn save_drink(State(state): State<AppState>, Json(payload): Json<Drink>) -> AppResult<Json<Value>> {
    let result: sqlx::Result<PgQueryResult> = sqlx::query!(
        "INSERT INTO user_drinks (user_id, timestamp) VALUES ($1, $2)",
        payload.user_id,
        payload.timestamp,
    ).execute(&state.pool).await;
    if result.is_err() {
        return Err(Error::DataUpdateFailed);
    }
    let body = Json(json!({
        "message": "Drink saved!",
    }));
    Ok(body)
}

#[debug_handler]
async fn get_drinks(State(state): State<AppState>) -> AppResult<Json<Vec<Drink>>> {
    let result: sqlx::Result<Vec<Drink>> = sqlx::query_as!(Drink, "SELECT user_id, timestamp FROM user_drinks").fetch_all(&state.pool).await;
    return match result {
        Err(_) => Err(Error::DataUpdateFailed),
        Ok(drinks) => Ok(Json(drinks)),
    }
}