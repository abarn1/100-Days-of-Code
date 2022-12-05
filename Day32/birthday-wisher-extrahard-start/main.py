##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt
import random
import re
import smtplib

BIRTHDAY_DF = pd.read_csv('birthdays.csv')
MONTH, DAY = dt.datetime.now().month, dt.datetime.now().day

NAME_EMAIL = {row['name']: row.email for index, row in BIRTHDAY_DF.iterrows() if row['month'] == MONTH and row['day'] == DAY}
LETTER_PATH = f'./letter_templates/letter_{random.randrange(1, 4)}.txt'

MY_EMAIL = '@gmail.com'
PASSWORD_LIST = pd.read_csv('../password.csv').to_dict(orient='records')
GMAIL_PASSWORD = [item['password'] for item in PASSWORD_LIST if item['item'] == 'gmail'][0]


def combine_text(message_list):
    # used to combine the multiple lines from using readlines to replace [NAME] in the message contents
    message_contents = ''
    for item in message_list:
        message_contents += item
    print(message_contents)
    return message_contents


def replace_name(letter, name):
    # original version of code to replace [NAME] in the message text files
    with open(letter) as email_text:
        message_text = []
        for line in email_text.readlines():
            message_text.append(re.sub("\[NAME]", name, line))
    return combine_text(message_text)


def replace_name2(letter, name):
    # more efficient version of the name replacing code from above
    with open(letter) as email_text:
        return re.sub("\[NAME]", name, email_text.read())


def send_birthday_message(birthday_message, recipient_email):
    # sets up the connection to gmail to send the birthday messages
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=recipient_email,
                            msg=f'Subject:Happy Birthday\n\n{birthday_message}')


for key, value in NAME_EMAIL.items():
    # for each of the people whose birthday it is: email them with the birthday message
    send_birthday_message(replace_name(LETTER_PATH, key), value)


