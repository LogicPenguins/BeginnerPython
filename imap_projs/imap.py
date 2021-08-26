#! python3
# imap.py - Testing out the imapclient.

import email
import imapclient
import os


site = "imap.gmail.com"
username = os.environ.get('xmexy_email')
password = os.environ.get('password')

server = imapclient.IMAPClient(site)
server.login(username, password)
server.select_folder("INBOX", readonly=True)

messages = server.search("FROM noreply@github.com")
for uid, message_data in server.fetch(messages, "RFC822").items():
    email_message = email.message_from_bytes(message_data[b"RFC822"])
    print('-.-.-.-.-.-.-.-.-.-.-.-.-.-.-')
    print(f"UID: {uid}\nFrom: {email_message.get('From')}\nSubject: {email_message.get('Subject')}\n\n")