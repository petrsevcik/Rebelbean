import smtplib
from decouple import config
from email.message import EmailMessage

SENDER_EMAIL = config("sender_email")
EMAIL_PASSWORD = config("email_password")
SERVER = config("server")
RECEIVER_EMAIL = config("receiver_email")

def send_email(message):
    sender_email = SENDER_EMAIL  # fill your email
    receiver_email = [RECEIVER_EMAIL] #recipients
    password = EMAIL_PASSWORD  #fill your password
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Rebelbean Alert'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    server = smtplib.SMTP_SSL(SERVER, 465) #choose your provider server
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    return "Email sent!"

# TEST
# print(send_email("Shreeeeded"))