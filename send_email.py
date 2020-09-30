#!/usr/bin/python3

import smtplib
import getpass

gmail_address = input("Type senders gmail address here: ")
print("Type your gmail password below")
password = getpass.getpass()
recipient = input("Type recipients email address here: ")
body_text = input("Type text content here: ")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_address, password)
server.sendmail(
  gmail_address,
  recipient,
  body_text)
server.quit()