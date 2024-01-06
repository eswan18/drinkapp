use axum::debug_handler;

#[debug_handler]
pub async fn get_hello() -> String {
    "hey!".to_string()
}