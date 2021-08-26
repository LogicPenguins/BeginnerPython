import smtplib
import os

server = smtplib.SMTP('smtp.gmail.com', 587)
user = os.environ.get('xmexy_email')
password = os.environ.get('password')

print('\n---Recipient Info---')
recipient = input('Recipient: ')
subject = input('Subject: ')
body = input('Email contents: ')

try:
    server.ehlo()
    server.starttls()
    server.login(user, password)
except:
    print('Something went wrong. Please try again.')

try:
    server.sendmail(user, recipient, f'Subject: {subject}\n{body}')
    print('Email was sent succesfully.')
    server.quit()
except:
    print('There was a problem sending the email. Please try again.')