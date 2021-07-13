import datetime as dt

import pytest

from drinkapi.models import Drink, UserSex

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


def near_equal(float_a: float, float_b: float) -> bool:
    '''
    Compare floats for near-equality.
    '''
    X = 0.0001
    return (float_a - X) < float_b < (float_a + X)


@pytest.mark.parametrize('drink', [drink for (drink, bac) in drinks_and_final_bacs])
def test_hours_since(drink: Drink):
    hours_since = (dt.datetime.now() - drink.time) / dt.timedelta(hours=1)
    assert near_equal(drink.hours_since, hours_since)


@pytest.mark.parametrize('drink,final_bac', drinks_and_final_bacs)
def test_decayed_bac(drink: Drink, final_bac: float):
    assert near_equal(drink.current_bac, final_bac)
