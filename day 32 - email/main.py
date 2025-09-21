import random
import smtplib
import datetime as dt

# app_password = "dxeznufbnagffhrh"
# orig_email = "mustafayigitisik749@gmail.com"
# receiver_email = "usa.mustafaisik@outlook.com"
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user= orig_email, password= app_password)
#     connection.sendmail(from_addr=orig_email, to_addrs=receiver_email, msg="Subject: Yeni Sezonda Fenerbahce\n\n 2025-26 sampiyonu")
# now = dt.datetime.now()
# print(now)

#challenge 1 - send quote emails every monday
with open("quotes.txt", 'r') as quotes_txt:
    quotes_arr = quotes_txt.readlines()

random_quote = random.choice(quotes_arr)
now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 6:
    app_password = "dxeznufbnagffhrh"
    orig_email = "mustafayigitisik749@gmail.com"
    receiver_email = "usa.mustafaisik@outlook.com"
    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp_connection:
        smtp_connection.starttls()
        smtp_connection.login(orig_email, app_password)
        smtp_connection.sendmail(from_addr=orig_email, to_addrs=receiver_email,
                                 msg=f"Subject: Quote of the Week\n\n{random_quote}".encode("utf-8"))



