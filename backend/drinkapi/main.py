from typing import List, Dict, Mapping
import datetime as dt
from uuid import uuid4
from collections import defaultdict

from fastapi import FastAPI, HTTPException

from .models import User, Drink


app = FastAPI()

users: Dict[str, User] = {}
drinks: Mapping[str, List[Drink]] = defaultdict(list)
used_usernames = set()


@app.get("/user/{user_id}")
def read_user(user_id: str):
    if user_id in users:
        user_dict = users[user_id].dict().copy()
        user_dict['user_id'] = user_id
        return user_dict
    else:
        if user_id not in users:
            raise HTTPException(status_code=404, detail='User not found')


@app.post('/user/', status_code=201)
def create_user(user: User):
    user_dict = user.dict().copy()
    username = user.username
    if username in used_usernames:
        raise HTTPException(
            status_code=409,
            detail='Requested username already exists'
        )
    user_id = str(uuid4())
    users[user_id] = user
    used_usernames.add(username)
    user_dict['user_id'] = user_id
    return user_dict


@app.get('/drink/{user_id}')
def read_drinks(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail='User not found')
    user_drinks = drinks[user_id]
    bac = sum([drink.current_bac for drink in user_drinks])
    return {'bac': bac}


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
