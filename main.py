from typing import Optional, List, Dict, Mapping
import datetime as dt
from uuid import uuid4
from collections import defaultdict

from fastapi import FastAPI

from .user import User
from .drink import Drink


app = FastAPI()

users: Dict[str, User] = {}
drinks: Mapping[str, List[Drink]] = defaultdict(list)
used_usernames = set()


@app.get("/users/{user_id}")
def read_user(user_id: str):
    if user_id in users:
        user = users[user_id]
        return {'user_id': user_id, 'username': user.username}
    else:
        return 404


@app.post('/users/')
def create_user(user: User):
    user_dict = user.dict()
    username = user.username
    if username in used_usernames:
        return 401
    user_id = str(uuid4())
    users[user_id] = user
    used_usernames.add(username)
    return user_dict, user_id


@app.post('/drinks/')
def create_drink(user_id: str, drink_grams: int):
    if user_id not in users:
        return 404
    user = Users[user_id].dict()
    user_wt_grams = user.wt_grams
    user_sex = user.sex
    drink = Drink(
        drinks_grams=drink_grams,
        user_wt_grams=user_wt_grams,
        user_sex=user_sex,
        time=dt.datetime.now()
    )
    drinks[user_id].append(drink)


@app.get('/drinks/{user_id}')
def read_drinks(user_id: str):
    bac = sum([drink.current_bac() for drink in drinks])
    return {'bac': bac}
