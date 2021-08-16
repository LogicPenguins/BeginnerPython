import pyinputplus as pyip
import random
import time

number_of_questions = 10
correct_answers = 0
for question_number in range(number_of_questions):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)

    prompt = '#%s: %s * %s = ' % (question_number, num1, num2)
    try:
        pyip.inputStr(prompt=prompt, allowRegexes=['^%s$' % (num1 * num2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_answers += 1
    time.sleep(3)
print('Score: %s / %s' % (correct_answers, number_of_questions))
