from enum import Enum

from pydantic import BaseModel


class UserSex(str, Enum):
    female = "female"
    male = "male"


class UserIn(BaseModel):
    username: str
    wt_grams: int
    sex: UserSex


class UserInDB(BaseModel):
    username: str
    wt_grams: int
    sex: UserSex
    id: str


class UserOut(BaseModel):
    username: str
    wt_grams: int
    sex: UserSex
    id: str
    bac: float = 0
