#! python3
# randomchore.py - Assigns and emails given emails random chores.

import pyinputplus as pyip
import random
import smtplib
import os

def assign_chores(info_list, chore_list):
    # GMAIL Server Setup.
    try:
        password = os.environ.get('password')
        username = os.environ.get('xmexy_email')
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(username, password)
    except smtplib.SMTPAuthenticationError:
        print('Authentication failed. Please restart program.')
    except TimeoutError:
        print('You took too long to respond. Please restart the program.')

    # Loop through contact infos and chores list and assign each email to a random chore (non repeated). 
    # Afterwards, send each email it's chore.
    while len(info_list) != 0:
        chosen_chore = random.choice(chore_list)
        chosen_person = random.choice(info_list)
        chosen_person_name = chosen_person.split('-')[0]
        chosen_person_email = chosen_person.split('-')[1]

        # Send email.
        try:
            print(f'Sending chore to {chosen_person_name}...')
            server.sendmail(username, chosen_person_email,
            f'Subject: {chosen_chore.upper()}\nHey there {chosen_person_name}. Your chore is to {chosen_chore}. Have fun!')
            
        except Exception as exc:
            print(f'An error occured when sending the chore to {chosen_person}:\n{exc}')

        # Remove chore that was chosen to avoid repetition.
        chore_list.remove(chosen_chore)
        info_list.remove(chosen_person)
    print('All emails were succesfully sent.')

chores = ['wash dishes', 'takeout trash', 'vacuum', 'walk dog']
info = [f"Duck-{os.environ.get('duck_email')}", f"Bcat{os.environ.get('bcat_email')}", f"Ahanaf-{os.environ.get('AZ_email')}"]


if __name__ == '__main__':
    assign_chores(info, chores)