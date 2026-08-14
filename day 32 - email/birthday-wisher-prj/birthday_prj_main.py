import random
from datetime import datetime as dt
import pandas as pd
import smtplib
from collections import defaultdict
#initialize today and constants
today = dt.now()
today_day_month = (today.month, today.day)
PLACEHOLDER = "[NAME]"
APP_PW = "dxeznufbnagffhrh"
ORIG_EMAIL = "mustafayigitisik749@gmail.com"

df = pd.read_csv("./birthdays.csv")
birthday_dict = defaultdict(list)
# alternative:
# birthday_dict = pd.read_csv("./birthdays.csv").to_dict(orient='records')
# for birthday in birthday_dict:
# if today == (birthday["month"], birthday["day"]):
for _,row in df.iterrows():
    birthday_dict[(row["month"], row["day"])].append(row)

if today_day_month in birthday_dict:
    for person in birthday_dict[today_day_month]:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as letter_file:
            letter_content = letter_file.read().replace(PLACEHOLDER, person["name"])
        receiver_email = person["email"]
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as smtp_connection:
                smtp_connection.starttls()
                smtp_connection.login(user=ORIG_EMAIL, password=APP_PW)
                smtp_connection.sendmail(from_addr=ORIG_EMAIL, to_addrs=receiver_email,
                                         msg=f"Subject: Happy Birthday\n\n{letter_content}".encode("utf-8"))
        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")

