import pandas
import os
import yagmail
from main import NewsFeed
import datetime


SENDER = os.environ.get("MYMAIL")
RECEIVER = os.environ.get("MYMAIL")
PASSWORD = os.environ.get("Gmail_PASSWORD")

df = pandas.read_excel(r'people.xlsx', sheet_name="Sheet 1")

today = datetime.datetime.now().strftime("%Y-%m-%d")
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

for index, row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    email = yagmail.SMTP(user=SENDER, password=PASSWORD)
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today!",
               contents=f"Hi, {row['name']} \n See what's on about {row['interest']} today. "
                        f"\n"
                        f"\n"
                        f"\n {news_feed.get()} "
                        f"\nHenri.")


