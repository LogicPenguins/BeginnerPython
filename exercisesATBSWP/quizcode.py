# This program will print 35 quizzes on the states in the US (written with help)

import random

capitals = {
    'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
    'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
    'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
    'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka',
    'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
    'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City',
    'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
    'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia',
    'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
    'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
    
for quiz_num in range(35):

    quiz_file = open(f'capitalsquiz{quiz_num + 1}.txt', 'w')
    answer_key_file = open(f'capitalsquiz_answers{quiz_num + 1}.txt', 'w')

    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write(f"{' ' * 20}State Capitals Quiz (Form {quiz_num + 1})")
    quiz_file.write('\n\n')

    states = list(capitals.keys()) 
    random.shuffle(states)  

    for question_num in range(50):
        
        correct_answer = capitals[states[question_num]]
        wrong_answers = list(capitals.values())  
        del wrong_answers[wrong_answers.index(correct_answer)]  
        wrong_answers = random.sample(wrong_answers, 3) 

        answer_options = wrong_answers + [correct_answer]
        random.shuffle(answer_options)

        quiz_file.write(f'{question_num + 1}. What is the capital of {states[question_num]}\n')
        for i in range(4):
            quiz_file.write(f"    {'ABCD'[i]}. { answer_options[i]}\n")
        quiz_file.write('\n')

        answer_key_file.write(f"{question_num + 1}. {'ABCD'[answer_options.index(correct_answer)]}\n")
    quiz_file.close()
    answer_key_file.close()