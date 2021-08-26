import imapclient
import imaplib
import os


imaplib._MAXLINE = 10000000

# Information setup.
username = os.environ.get('xmexy_email')
password = os.environ.get('password')
site = 'imap.gmail.com'

# Logging into server and selecting folder to search.
server = imapclient.IMAPClient(site)
server.login(username, password)
server.select_folder('INBOX', readonly=False)

# Deleting emails sent from robot@openweathermap.org 
try:
    UIDs = server.search('FROM robot@openweathermap.org')
    server.delete_messages(UIDs)
    print('Given emails deleted succesfully.')
    server.logout()

except Exception as exc:
    print(f'There was an error: {exc}')
    server.logout()