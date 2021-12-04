from sport_generator import RandomCardio, RandomBodyPart
import pandas as pd
from datetime import date, timedelta
import random
from tabulate import tabulate
from typing import List

def create_schedule(start: date, end: date)->pd.DataFrame:
    """given a number of weeks generate a schedule"""
    num_days = (end - start).days
    rest_day = random.randint(1,7)
    random_cardio = RandomCardio()
    rand_body_part = RandomBodyPart()
    cardio = []
    weights = []
    dates = []
    for i in range(num_days+1):
        dates.append(start + timedelta(days=i))
        if i % 7 == rest_day:
            cardio.append("rest")
            weights.append("rest")
        else:
            cardio.append(random_cardio.next())
            weights.append(rand_body_part.next())
    return pd.DataFrame({'day':dates, 'cardio_activity': cardio, 'focus_part': weights})

def save_schedule(start: date, end: date):
    """save a schedule to csv"""
    df = create_schedule(start, end)
    df.to_csv("schedule.csv",index=False)

def get_schedule()->pd.DataFrame:
    return pd.read_csv("schedule.csv")

def get_today_schedule():
    """print the schedule of specific days"""
    df = get_schedule()
    df.set_index("day",inplace=True)
    df = df[df.index==str(date.today())]
    print(tabulate(df, headers="keys",tablefmt="psql",showindex=True))
