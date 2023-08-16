import smtplib
import datetime as dt
import random as r

# ---working code aswell as notes--- 

my_email = 'mail@gmail.com'
app_pw = 'password'

# connection = smtplib.SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=app_pw)
# connection.sendmail(from_addr=my_email, to_addrs='mail@gmail.com', msg='Subject:Hello From Python\n\nThis is the body of the email')
# connection.close()

# with smtplib.SMTP('smtp.gmail.com') as con:
#     con.starttls()
#     con.login(user=my_email, password=app_pw)
#     con.sendmail(from_addr=my_email, to_addrs='mail@gmail.com', msg='Subject:Hello From Python\n\nThis is the body of the email')

# now = dt.datetime.now() # gets current time
# print (now.weekday)
# bday = dt.datetime(year=1000, month=12, day=1)

# -- monday motivational quotes --

today = dt.datetime.now()
birthday = dt.datetime(year=2000, month=12, day=10)

if today.weekday() == 0: # emails a motivational quote each monday
    
    contents = []
    with open('quotes.txt', mode='r') as file:
        contents = file.readlines()
    
    quote = r.choice(contents)
    with smtplib.SMTP('smtp.gmail.com') as con:
        con.starttls()
        con.login(user=my_email, password=app_pw)
        con.sendmail(from_addr=my_email, to_addrs='mail@gmail.com', msg=f'Subject:Motivational Quote\n\n{quote}')

birthday = dt.datetime(year=2000, month=12, day=10)

# --- birth day message --- 
if today.month == birthday.month and today.day == birthday.day:
    with smtplib.SMTP('smtp.gmail.com') as con:
        con.starttls()
        con.login(user=my_email, password=app_pw)
        con.sendmail(from_addr=my_email, to_addrs='mail@gmail.com', msg=f'Subject:Happy Birthday\n\nHAPPY BIRTHDAY!')


# use pythonanywhere (website) to run the code as a scheduled task (or create one locally)
