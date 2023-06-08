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
   
while True:
    for website in websites:
        try:
            response = requests.get(website['url'])
            if response.status_code != 200:
                send_email(f'{website["name"]} is down!', f'{website["name"]} is not responding. Status code: {response.status_code}')
        except requests.exceptions.RequestException:
            send_email(f'{website["name"]} is down!', f'{website["name"]} is not responding. Connection error.') 
            
    time.sleep(60) # Check every minute       
