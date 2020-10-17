#!/usr/bin/python3

import smtplib
import getpass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

gmail_address = input("Type senders gmail address here: ")
password = getpass.getpass()
recipient = input("Type recipients email address here: ")
file = input("Type attachment file location here: ")

message = MIMEMultipart()
message["From"] = gmail_address
message['To'] = recipient
message['Subject'] = "sending mail using python"
#file = "doc.txt"
attachment = open(file,'rb')

obj = MIMEBase('application','octet-stream')
obj.set_payload((attachment).read())
encoders.encode_base64(obj)
obj.add_header('Content-Disposition',"attachment; filename= "+file)
message.attach(obj)

my_message = message.as_string()
email_session = smtplib.SMTP('smtp.gmail.com',587)
email_session.starttls()
email_session.login(gmail_address,password)
email_session.sendmail(gmail_address, recipient, my_message)
email_session.quit()
print("YOUR MAIL HAS BEEN SENT SUCCESSFULLY")