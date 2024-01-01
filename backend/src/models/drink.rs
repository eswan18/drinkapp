use uuid::Uuid;
use serde_derive::{Deserialize, Serialize};
use chrono::{DateTime, Utc};

#[derive(Deserialize, Serialize, Debug)]
pub struct Drink {
    timestamp: DateTime<Utc>,
    user_id: Uuid,
}