from typing import List, Dict, Mapping
import datetime as dt
from uuid import uuid4
from collections import defaultdict

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import UserIn, UserInDB, UserOut, Drink

ORIGINS = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables that should eventually be tables in some kind of database.
users: Dict[str, UserInDB] = {}
drinks: Mapping[str, List[Drink]] = defaultdict(list)
used_usernames = set()


def get_user_bac(user_id: str) -> float:
    bac = sum([drink.current_bac for drink in drinks[user_id]])
    return bac


@app.get("/user/{user_id}", response_model=UserOut)
def read_user(user_id: str) -> UserOut:
    if user_id in users:
        user_in_db = users[user_id]
        bac = get_user_bac(user_id=user_id)
        user_out = UserOut(**user_in_db.dict(), bac=bac)
        return user_out
    else:
        raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/', status_code=201, response_model=UserOut)
def create_user(user: UserIn) -> UserInDB:
    if user.username in used_usernames:
        raise HTTPException(
            status_code=409,
            detail='Requested username already exists'
        )
    user_id = str(uuid4())
    user_in_db = UserInDB(**user.dict(), id=user_id)
    users[user_id] = user_in_db
    used_usernames.add(user.username)
    return user_in_db


@app.get('/drink/{user_id}', response_model=List[Drink])
def read_drinks(user_id: str) -> List[Drink]:
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    user_drinks = drinks[user_id]
    return user_drinks


@app.post('/drink/', status_code=201)
def create_drink(user_id: str, drink_grams: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    user = users[user_id]
    user_wt_grams = user.wt_grams
    user_sex = user.sex
    drink = Drink(
        drink_grams=drink_grams,
        user_wt_grams=user_wt_grams,
        user_sex=user_sex,
        time=dt.datetime.now()
    )
    drinks[user_id].append(drink)
