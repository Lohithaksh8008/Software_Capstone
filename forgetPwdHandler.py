import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def forgotPswdEmailHandler(receiver, msg):
    sender_address = 'vaidyasreeganesh@gmail.com'
    sender_pass = 'Sreeganesh@87'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver
    message['Subject'] = 'Commerce Bank'
    message.attach(MIMEText(msg, 'plain'))

    ses = smtplib.SMTP('smtp.gmail.com', 587)
    ses.starttls()
    ses.login(sender_address, sender_pass)
    ses.sendmail(sender_address, receiver, message.as_string())
    ses.quit()
