# Write a function that checks whether a number is ina given range (inclusive of high and low)

def range_check(num, low, high):
    if num > low and num < high:
        print(f'{num} is in the range between {low} and {high}.')
    else:
        print(f'{num} is not in the range between {low} and {high}.')

range_check(5, 0, 3)