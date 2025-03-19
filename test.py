import smtplib
import os

USERNAME = os.getenv('GMAIL_USERNAME')
PWD = os.getenv('GMAIL_PWD')
SERVER = os.getenv('SMTP_SERVER')

try:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_server:
        smtp_server.connect('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(USERNAME, PWD)
        print("Login successful!")
        smtp_server.quit()
except smtplib.SMTPAuthenticationError as e:
    print(f"Authentication failed: {e}")