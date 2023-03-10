import pandas
import os
import yagmail

SENDER = os.environ.get("MYMAIL")
RECEIVER = os.environ.get("MYMAIL")
PASSWORD = os.environ.get("Gmail_PASSWORD")

email = yagmail.SMTP(user=SENDER, password=PASSWORD)
email.send(to=RECEIVER,
           subject="Hi There",
           contents="Hi, this is a body of the email \nHenri.",
           attachments="design.txt")

# if __name__ == "__main__":
#     pass
