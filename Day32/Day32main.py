import smtplib
import pandas as pd

my_email = '@gmail.com'
password_list = pd.read_csv('password.csv').to_dict(orient='records')
gmail_password = [item['password'] for item in password_list if item['item'] == 'gmail'][0]

with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=gmail_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs='@gmail.com',
                        msg='Subject:Hello\n\nHello')
