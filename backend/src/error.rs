use axum::response::{IntoResponse, Response};
use http::StatusCode;

// From https://github.com/tokio-rs/axum/blob/c486cc8207a98a015aca76cb84f26ab1c6940d83/examples/anyhow-error-response/src/main.rs

pub enum Error {
    LoginFailed,
    DataUpdateFailed
}

pub type AppResult<T> = core::result::Result<T, Error>;

impl IntoResponse for Error {
    fn into_response(self) -> Response {
        match self {
            Error::LoginFailed => {
                (
                    StatusCode::UNAUTHORIZED,
                    "Invalid username or password",
                )
                    .into_response()
            },
            Error::DataUpdateFailed => {
                (
                    StatusCode::INTERNAL_SERVER_ERROR,
                    "Unable to update data",
                )
                    .into_response()
            }
        }
    }
}