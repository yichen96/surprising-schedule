from sport_generator import RandomCardio, RandomBodyPart
import pandas as pd
from datetime import date, timedelta, datetime
import random
from tabulate import tabulate
from typing import List
from PyInquirer import prompt

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

def ask_mode():
    mode_prompt = {
        'type': 'list',
        'name': 'mode',
        'message': 'Menu',
        'choices': ["Today's schedule", "Create new schedule"],
        'default': "Today's schedule"
    }
    answers = prompt(mode_prompt)
    return answers['mode']

def ask_date():
    date_prompt = [{
        'type': 'input',
        'name': 'start_date',
        'message': 'When does your schedule begin? (yyyy-mm-dd)',
        'filter': lambda x: datetime.strptime(x,"%Y-%m-%d").date()
    },{
        'type': 'input',
        'name': 'end_date',
        'message': 'When does your schedule end? (yyyy-mm-dd)',
        'filter': lambda x: datetime.strptime(x,"%Y-%m-%d").date()
    }]
    answers = prompt(date_prompt)
    return answers

def main():
    logo = ' \n' + '                           _          \n' + ' ___ _   _ _ __ _ __  _ __(_)___  ___ \n' + '/ __| | | | \'__| \'_ \| \'__| / __|/ _ \\\n' + '\__ \ |_| | |  | |_) | |  | \__ \  __/\n' + '|___/\__,_|_|  | .__/|_|  |_|___/\___|\n' +'               |_|                    \n'
    print(logo)
    mode = ask_mode()
    if mode == "Create new schedule":
        date_answer = ask_date()
        save_schedule(date_answer['start_date'],date_answer['end_date'])
        print("FYI today's schedule:")
        get_today_schedule()
    else:
        get_today_schedule()

if __name__ == "__main__":
    main()