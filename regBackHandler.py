import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def emailHandler(receiver):
    sr = 'BANK'
    n = random.randint(0, 1000)
    s = sr + str(n)
    msg = 'Thanks for choosing online Banking.\nCustomer Id is: {}.\n\n Regards,\nOnline Bank Service'.format(s)

    sender_address = 'vaidyasreeganesh@gmail.com'
    sender_pass = 'Sreeganesh@87'

    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver
    message['Subject'] = 'E- Commerce Bank'
    message.attach(MIMEText(msg, 'plain'))

    ses = smtplib.SMTP('smtp.gmail.com', 587)
    ses.starttls()
    ses.login(sender_address, sender_pass)
    text = message.as_string()
    ses.sendmail(sender_address, receiver, text)
    ses.quit()
    return s
