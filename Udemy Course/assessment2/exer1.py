# use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

for word in st.lower().split():
    if word.startswith('s'):
        print(word)
    # This else statement is optional, but it's nice to have for beginners to understand what happens 
    # if the above if statement's condition is not met.
    else:
        continue