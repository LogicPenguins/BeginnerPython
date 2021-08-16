import random

trivia = [
    ('Which bear lives at the North Pole?', 'polar bear'),
    ('Which is the fastest land animal?', 'cheetah'),
    ('Which is the largest animal?', 'blue whale'),
    ('Which one of these is a fish? A) Whale \n B) Dolphin \n, C) Shark \n D) Squid \n Type A, B, C, or D', 'C')
]

print("Welcome to the guessing game. Answer the questions to the best of your ability.")
guess_limit = 3
attempts = 0
score = 0
attempts_count = 0
still_guessing = False

while attempts < guess_limit:
    attempts += 1
    if not still_guessing:
        question, correct_answer = random.choice(trivia)
        print(question)
        user_answer = input()
    elif still_guessing:
        print(question)
        user_answer = input()
    if user_answer == correct_answer:
        print("You got it right! +1 score")
        score += 1 - attempts_count
        attempts_count = 0
        print(score)
        still_guessing = False
    elif user_answer != correct_answer:
        print("You got it wrong. Please try again.")
        attempts_count += 1
        still_guessing = True

