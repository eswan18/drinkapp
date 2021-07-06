import datetime as dt
from dataclasses import dataclass

from .user import UserSex


@dataclass
class Drink:
    drink_grams: int
    user_wt_grams: int
    user_sex: UserSex 
    time: dt.datetime

    @property
    def hours_since(self):
        now = dt.datetime.now()
        time_since = now - self.time
        return time_since / dt.timedelta(hours=1)

    def decayed_bac(self, decay_hrs: float):
        r = 0.55 if self.user_sex == UserSex.female else 0.68
        initial_bac = self.drink_grams / (self.user_wt_grams * r)
        updated_bac = initial_bac - (0.015 * decay_hours)
        return updated_bac

    @property
    def current_bac(self):
        '''
        Get the current BAC effect of this drink.

        Uses the Widmark formula.
        '''
        return self.decayed_bac(decay_hrs=self.hours_since)

