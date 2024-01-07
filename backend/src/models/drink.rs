use uuid::Uuid;
use serde_derive::{Deserialize, Serialize};
use chrono::NaiveDateTime;

#[derive(Deserialize, Serialize, Debug)]
pub struct Drink {
    pub timestamp: NaiveDateTime,
    pub user_id: Uuid,
}