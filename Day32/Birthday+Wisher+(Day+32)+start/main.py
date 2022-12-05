import smtplib
import pandas as pd
import datetime as dt
import random

NOW = dt.datetime.now()
DAY_OF_WEEK = NOW.weekday()

MY_EMAIL = '@gmail.com'
PASSWORD_LIST = pd.read_csv('../password.csv').to_dict(orient='records')
GMAIL_PASSWORD = [item['password'] for item in PASSWORD_LIST if item['item'] == 'gmail'][0]


def get_motivation():
    with open('quotes.txt', 'r') as quotes:
        lines = quotes.readlines()
        return random.choice(lines)


def send_motivation():
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs='@gmail.com',
                            msg=f'Subject:Motivation\n\n{get_motivation()}')


if DAY_OF_WEEK == 6:
    send_motivation()

