import datetime as dt
from typing import Dict

import pytest

from drinkapi.drink import Drink
from drinkapi.user import UserSex

drinks_and_final_bacs = [
    (
        Drink(
            drink_grams=56,
            user_wt_grams=54480,
            user_sex=UserSex.female,
            time=dt.datetime.now() - dt.timedelta(hours=5)
        ),
        0.11189,
    )
]


def near_equal(float_a, float_b):
    '''
    Compare floats for near-equality.
    '''
    X = 0.0001
    return (float_a - X) < float_b < (float_a + X)

@pytest.mark.parametrize('drink', [drink for (drink, bac) in drinks_and_final_bacs])
def test_hours_since(drink):
    hours_since = (dt.datetime.now() - drink.time) / dt.timedelta(hours=1)
    assert near_equal(drink.hours_since, hours_since)

@pytest.mark.parametrize('drink,final_bac', drinks_and_final_bacs)
def test_decayed_bac(drink, final_bac):
    assert near_equal(drink.current_bac, final_bac)
