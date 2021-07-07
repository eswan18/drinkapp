from enum import Enum

from pydantic import BaseModel


class UserSex(str, Enum):
    female = "female"
    male = "male"


class User(BaseModel):
    username: str
    wt_grams: int
    sex: UserSex
