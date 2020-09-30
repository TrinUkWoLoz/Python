#!/usr/bin/python3

import smtplib
import getpass

print("Type your gmail password below")
password = getpass.getpass()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("triniwizard@gmail.com", password)
server.sendmail(
  "triniwizard@gmail.com",
  "triniwizard@gmail.com",
  "This message is from a wizards python script - testing tester 123")
server.quit()