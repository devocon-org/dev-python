import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_alert_email(subject, body, recipient_email):
    sender_email = "your-email@example.com"
    password = "your-email-password"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            print(f"Alert email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_disk_usage(threshold=80):
    disk_usage = psutil.disk_usage('/')
    if disk_usage.percent > threshold:
        print(f"Disk usage is above {threshold}%! Sending alert.")
        send_alert_email(
            subject="Disk Usage Alert",
            body=f"Disk usage has exceeded {threshold}% on the server. Current usage: {disk_usage.percent}%",
            recipient_email="recipient@example.com"
        )

if __name__ == '__main__':
    check_disk_usage()
