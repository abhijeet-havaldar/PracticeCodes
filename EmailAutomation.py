import smtplib
from email.mime.text import MIMEText

sender = "youremail@gmail.com"
password = "yourpassword"
receiver = input("Enter reciver email: ")

subject = input("Subject: ")
body = input("Message: ")

msg = MIMEText(body)
msg['Subject'] = subject
msg['from'] = sender
msg["To"] = receiver

server = smtplib.SMTP_ssl('smtp.gmail.com',465)
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()

print("✅ Email sent successfully!")