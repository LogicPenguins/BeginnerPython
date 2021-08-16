import pyinputplus as pyip
import sys
import time


prices = {
    'bread types': {
        'wheat': 1,
        'white': 2,
        'sourdough': 1
    },
    'protein types': {
        'chicken': 2,
        'turkey': 3,
        'ham': 2,
        'tofu': 1.5
    },
    'cheese types': {
        'cheddar': 1,
        'Swiss': 0.5,
        'mozarella': 0.7
    },
    'toppings': {
        'mayo': 0.5,
        'mustard': 0.5,
        'lettuce': 1,
        'tomato': 0.8
    } 
    
}
start_program = pyip.inputYesNo("Would you like to start the program? ")


if start_program == 'yes':
    all_items = []
    total_cost = 0
    print('''
    Welcome to the Python Sandwich Maker!
    We will ask you some questions for your 
    sandwich preferences. Then we will evaluate 
    your choices and make you the perfect sandwich!
    We hope you enjoy our program :]
    ''')
    time.sleep(3)
    
    print('First tell me, what type of bread would you like?')
    all_items.append(pyip.inputMenu(['wheat', 'white', 'sourdough']))

    print('Awesome choice! Next, what type of protein do you want in your sandwich?')
    all_items.append(pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu']))

    cheese = pyip.inputYesNo('Amazing! Do you want cheese with your sandwich? ')
    if cheese == 'yes':
        print('Alright, cool. What kind of cheese?')
        all_items.append(pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella']))
    else:
        print('Alright no cheese it is!')
    mayo = pyip.inputYesNo('Do you want mayo on your sandwich? ')
    if mayo == 'yes':
        all_items.append('mayo')
    else:
        pass
    mustard = pyip.inputYesNo('Do you want mustard on your sandwich? ')
    if mustard == 'yes':
        all_items.append('mustard')
    else:
        pass
    lettuce = pyip.inputYesNo('Do you want lettuce with your sandwich? ')
    if lettuce == 'yes':
        all_items.append('lettuce')
    else:
        pass
    tomato = pyip.inputYesNo('Do you want tomato with your sandwich? ')
    if tomato == 'yes':
        all_items.append('tomato')
    else:
        pass
    print('''
    Alright we\'re almost done! 
    Now just tell me how many 
    sandwiches you want, and I\'ll 
    get everything ready! 
    ''')
    sandwich_amount = pyip.inputInt('Amount of sandwiches: ', min = 1)
    for item in all_items: 
        for key in prices.keys():
            try:
                all_items[all_items.index(item)] = prices[key][item]
            except:
                pass
    for item in all_items:
        total_cost += item
    total_cost *= sandwich_amount
    print(f'The total cost of your sandwich will be ${total_cost}. Thank you for making a sandwich with us!')
else:
    print('Alright, have a wonderful day!')
    sys.exit()