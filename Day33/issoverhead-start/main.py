import requests
from datetime import datetime
import smtplib
import pandas as pd

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    return MY_LONG + 5 >= iss_longitude >= MY_LONG - 5 and MY_LAT + 5 >= iss_latitude >= MY_LAT - 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()


def is_dark():
    return time_now.hour <= sunrise or time_now.hour >= sunset

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


MY_EMAIL = '@gmail.com'
PASSWORD_LIST = pd.read_csv('../../Day32/password.csv').to_dict(orient='records')
GMAIL_PASSWORD = [item['password'] for item in PASSWORD_LIST if item['item'] == 'gmail'][0]


def iss_message():
    # sets up the connection to gmail to send the iss is overhead messages
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=GMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f'Subject:ISS Warning\n\nThe ISS is overhead right now. Go check it out')


if is_dark() and is_close():
    iss_message()
