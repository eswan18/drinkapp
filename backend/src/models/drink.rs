use uuid::Uuid;
use serde_derive::{Deserialize, Serialize};
use chrono::{DateTime, Utc};

#[derive(Deserialize, Serialize, Debug)]
pub struct Drink {
    pub timestamp: DateTime<Utc>,
    pub user_id: Uuid,
}