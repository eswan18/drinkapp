use chrono::NaiveDateTime;
use serde_derive::{Deserialize, Serialize};
use uuid::Uuid;

#[derive(Deserialize, Serialize, Debug)]
pub struct Drink {
    pub timestamp: NaiveDateTime,
    pub user_id: Uuid,
}
