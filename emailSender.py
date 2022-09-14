from email.message import  EmailMessage
from accountDetail import *
import ssl
import smtplib

emailSender = email
emailPassword = password

emailReceiver = receiver

subject = "Hi testing sending email"
body = """
Is this thing on?
"""

em = EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(emailSender, emailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())

print("Finished sending email")
