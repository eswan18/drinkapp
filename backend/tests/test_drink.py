import datetime as dt
from typing import Dict

import pytest

from drinkapi.drink import Drink
from drinkapi.user import UserSex

def near_equal(float_a, float_b):
    '''
    Compare floats for near-equality.
    '''
    X = 0.0001
    return (float_a - X) < float_b < (float_a + X)

def test_hours_since():
    an_hour_ago = dt.datetime.now() - dt.timedelta(hours=1)
    drink = Drink(3, 3943, UserSex.male, time=an_hour_ago)
    assert 0.99 <= drink.hours_since <= 1.01

@pytest.mark.parametrize(
    'args,hrs,expected',
    [
        pytest.param((56, 54480, UserSex.female, dt.datetime.now()), 5, 0.11189)
    ],
)
def test_decayed_bac(args: Dict, hrs: float, expected: float):
    drink = Drink(*args)
    assert near_equal(drink.decayed_bac(hrs), expected)
