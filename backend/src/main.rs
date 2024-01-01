use axum::Router;

mod routes;
mod handlers;
mod models;

#[tokio::main]
async fn main() {
    let app = Router::new()
        .merge(routes::app_routes());

    axum::Server::bind(&"127.0.0.1:3000".parse().unwrap())
        .serve(app.into_make_service())
        .await
        .unwrap();
}
