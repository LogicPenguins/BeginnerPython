# Use List Comprehension to create a list of the first letters of eveyr word in the string below.

st = 'Create a list of the first letters of the first letters of every word in this string'

first_letters = [word[0] for word in st.split()]
print(first_letters)