#! python3
# umbrella_reminder.py - Will remind you to bring an umbrella when the day's weather is rainy.

from twilio.rest import Client
import datetime
import time
import os
import bs4
import requests


def check_for_rain():
    try:
        url = 'https://weather.com/weather/today/l/8c6546459d44852f4b600504ef5c3197304de882acc9f479c96488d58474347b'
        forecast_data = requests.get(url)
        forecast_data.raise_for_status()
        soup = bs4.BeautifulSoup(forecast_data.text, 'html.parser')
        current_forecast_html = soup.find_all("div", {"data-testid": "wxPhrase"})
        current_forecast = current_forecast_html[0].get_text()

        if current_forecast == 'Rain':
            msg_content = "The weather forecast currently shows rain. Don't forget to bring an umbrella!"

            account_SID = os.environ.get('twilio_SID')
            auth_token = os.environ.get('twilio_auth_token')
            my_twilio_number = os.environ.get('twilio_phone_num')
            my_cell_number = os.environ.get('my_phone_num')

            twilio_cli = Client(account_SID, auth_token)
            twilio_cli.messages.create(body=msg_content, from_=my_twilio_number, to=my_cell_number)
            print('Rain detected. A notification was sent.')
        else:
            print('Currently no rain.')

    except requests.exceptions.HTTPError:
        print('URL failed/forbidden. Please try again.')

# Initial values must be adjusted to fit user accordingly. Program will handle future dates.
year = 2021
month = 8
day = 26
while True:
    # This while loop will run until it is manually terminated, checking the weather at given link location
    # Everyday at 12 PM. Change datetime values as needed.
    current_date = datetime.datetime(year, month, day, 12, 0, 0)
    while datetime.datetime.now() < current_date:
        time.sleep(1)
    check_for_rain()
    day += 1
    if month == 12:
        if day == 31:
            year += 1
            month = 1
            day = 1
    # Change max days accordingly
    if day == 31:
        day = 0
        month += 1

    


