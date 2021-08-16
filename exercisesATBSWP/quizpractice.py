# coded all without reference to Automate the Boring Stuff, I am very proud :]

import random

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
    'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
    'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
    'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
    'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
    'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
    'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
    'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
    'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
    'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
    'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
    'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
    'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
    'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quiz_num in range(35):
    quiz_file = open(f'capitalsquiz{quiz_num+1}', 'w')
    quiz_answers = open(f'answerkey{quiz_num+1}', 'w')
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(f"{' ' * 20} UNITED STATES CAPITALS QUIZ\n{'-' * 60}\n\n")
    states = list(capitals.keys())
    random.shuffle(states)
    for quiz_question in range(50):
        correct_answer = capitals[states[quiz_question]]
        wrong_answer = list(capitals.values())
        wrong_answer.remove(correct_answer)
        wrong_answers = random.sample(wrong_answer, 3)
        options_final = wrong_answers + [correct_answer]
        random.shuffle(options_final)
        quiz_file.write(f'{quiz_question + 1}. What is the capital of {states[quiz_question]}?\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. {  options_final[i]}\n\n")
        quiz_answers.write(f"{quiz_question + 1}. {'ABCD'[options_final.index(correct_answer)]}\n\n")
    quiz_file.close()
    quiz_answers.close()

