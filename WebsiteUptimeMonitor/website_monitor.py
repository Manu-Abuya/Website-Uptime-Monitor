import requests
import time
import smtplib

# UptimeRobot API Key
API_KEY = 'YOUR_UPTIMEROBOT_API_KEY'

# List of websites to monitor
websites = [
    {'name': 'Example', 'url': 'https://example.com'},
    {'name': 'Google', 'url': 'https://google.com'},
    {'name': 'Jumia', 'url': 'https://www.jumia.co.ke/'},
]

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS'
EMAIL_PASSWORD = 'YOUR_EMAIL_PASSWORD'
RECIPIENT_ADDRESS = 'RECIPIENT_EMAIL_ADDRESS'

def send_email(subject, body):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp,login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        message = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(EMAIL_ADDRESS, RECIPIENT_ADDRESS, message)
        
