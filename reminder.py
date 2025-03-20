# This script sends an email to remind me that I should update my to-do list at 10:30pm
import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

# Set up env variables
USERNAME = os.getenv('GMAIL_USERNAME')
PWD = os.getenv('GMAIL_PWD')
SERVER = 'smtp.gmail.com'
SENDER = os.getenv('EMAIL_SENDER')
RECEIVER = os.getenv('EMAIL_RECEIVER')

subject = 'Reminder to update your todo list in todo.json'
body = "Hi there Dee. Please update your to do list in todo.json to be sent to you by 7:30AM tomorrow. Have a good night sleep."

def send_email(subject, body, sender, server, receiver, pwd):
    msg = MIMEText(body)
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject


    try:
        with smtplib.SMTP(server, 587) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()

            smtp_server.login(sender, pwd)
            print('Login successful!')
            smtp_server.sendmail(sender, receiver, msg.as_string())

        print("Email sent successfully!")

    except Exception as e:
        print(f'Failed to send email: {e}')


if __name__ == "__main__":
    send_email(subject=subject, body=body, sender=SENDER, receiver=RECEIVER, server=SERVER, pwd=PWD)

