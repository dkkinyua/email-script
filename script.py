import json
import os
import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('GMAIL_USERNAME')
PWD = os.getenv('GMAIL_PWD')
SERVER = 'smtp.gmail.com'
SENDER = os.getenv('EMAIL_SENDER')
RECEIVER = os.getenv('EMAIL_RECEIVER')

subject = 'To-do list for today and Daily Bible Verse'

# Fetch the Bible verse from API
url = 'https://beta.ourmanna.com/api/v1/get?format=json&order=daily'
headers = {"accept": "application/json"}
response = requests.get(url, headers=headers)
bible_data = response.json()

bible_verse = bible_data["verse"]["details"]["text"]
bible_chapter = bible_data["verse"]["details"]["reference"]

# Load the to-do list from JSON file
with open('todo.json', 'r') as f:
    todo_data = json.load(f)

# Construct the HTML email body
body = """\
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 10px; text-align: left; }
        th { background-color: #f2f2f2; }
        h2 { color: #2c3e50; }
        h3 { color: #16a085; }
        p { font-size: 16px; }
    </style>
</head>
<body>
    <h2>📌 Today's To-Do List</h2>
    <table>
        <tr><th>Time</th><th>Tasks</th></tr>
"""

# Append to-do tasks to the table
for entry in todo_data:
    tasks = "<br>".join(entry['to-do'])
    body += f"<tr><td><b>{entry['time']}</b></td><td>{tasks}</td></tr>"

body += f"""\
    </table>
    <br>
    <h3>📖 Daily Bible Verse</h3>
    <p><i>{bible_chapter}</i> — <b>{bible_verse}</b></p>
</body>
</html>
"""

def send_email(subject, receiver, sender, body, pwd, server):
    msg = MIMEText(body, "html")  # Set content type to HTML
    msg["Subject"] = subject
    msg["To"] = receiver
    msg["From"] = sender

    try:
        with smtplib.SMTP(server, 587) as smtp_server:
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.ehlo()

            smtp_server.login(sender, pwd)
            print('Login successful!')
            smtp_server.sendmail(sender, receiver, msg.as_string())

        print("Email has been sent successfully!")
    except Exception as e:
        print(f'Failed to send email: {e}')

# print(SENDER)
# print(SERVER)

# Send the email
if __name__ == "__main__":
    send_email(subject=subject, receiver=RECEIVER, sender=SENDER, body=body, pwd=PWD, server=SERVER)
