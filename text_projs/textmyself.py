#! python3
# textmyself.py - Defines the textmyself() function that texts a message passed
# to it as a string.

from twilio.rest import Client
import os

# Preset Values:
accountSID = os.environ.get('twilio_SID')
auth_token = os.environ.get('twilio_auth_token')
my_twilio_number = os.environ.get('twilio_phone_num')
my_cell_phone = os.environ.get('my_phone_num')

# Call this function and pass it a string to then text to the phone number.
def text_my_self(message):
    twilio_cli = Client(accountSID, auth_token)
    twilio_cli.messages.create(body=message, from_=my_twilio_number, to=my_cell_phone)