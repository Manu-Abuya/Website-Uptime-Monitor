# Website Uptime Monitor

This is a simple Python script that periodically checks the availability of websites or services and sends notifications when downtime is detected. It utilizes the UptimeRobot API to check the website status and sends email notifications using Gmail's SMTP server.

## Features

- Monitors the uptime of multiple websites or services
- Sends email notifications when a website/service is down
- Easy configuration of websites to monitor
- Adjustable monitoring interval (default: 1 minute)
- Customizable email notification messages

## Prerequisites

- Python (version 3.6 or higher)
- `requests` library
- Gmail account (for sending email notifications)

## Getting Started

1. Clone the repository:
    ```shell
    git clone https://github.com/Manu-Abuya/Website-Uptime-Monitor.git
    ```

2. Install the required libraries:
    ```shell
    pip install requests
    ```
    

3. Set up the UptimeRobot API:

    - Create an UptimeRobot account at https://uptimerobot.com/ if you haven't already.
    - Obtain your API key from the "My Settings" section of your UptimeRobot account.

4. Set up Gmail SMTP:

    - Create a Gmail account if you don't have one.
    - Enable "Less Secure Apps" access in your Gmail account settings or set up an app password for enhanced security.

5. Configure the script:

    - Open `website_monitor.py` in a text editor.
    - Replace `'YOUR_UPTIMEROBOT_API_KEY'` with your UptimeRobot API key.
    - Replace `'YOUR_EMAIL_ADDRESS'` and `'YOUR_EMAIL_PASSWORD'` with your Gmail account credentials.
    - Replace `'RECIPIENT_EMAIL_ADDRESS'` with the email address where you want to receive notifications.

6. Run the script:

    ```shell
    python website_monitor.py
    ```
    
 
The script will start monitoring the websites at the specified interval (default: 1 minute). You will receive email notifications whenever a website goes down.

## Customization

- To monitor additional websites, add them to the `websites` list in `website_monitor.py` with the desired name and URL.
- You can adjust the monitoring interval by changing the value in the `time.sleep()` function (in seconds).
- Modify the email notification messages in the `send_email()` function to suit your preferences.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project was inspired by the need for a simple and lightweight website uptime monitoring solution. It utilizes the UptimeRobot API for website status checks and Gmail's SMTP server for email notifications.

Feel free to contribute, open issues, or provide feedback to help improve this project.




