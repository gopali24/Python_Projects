import os
import random
import smtplib

def automatic_email():
    user=input("Enter your name: ")
    email=input("Enter your email-id: ")
    msg = (f"Dear {user}, this is an auto generated mail. Please do not reply")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("gopalikshitij@gmail.com","luorerounhodhdfi")
    s.sendmail('&&&&&&&&&&&', email, msg)
    print("Email sent!!")

automatic_email()