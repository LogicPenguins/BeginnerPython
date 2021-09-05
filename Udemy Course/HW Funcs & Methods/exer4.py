# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def uniquer(lst):
    uniques = []
    for item in lst:
        if item not in uniques:
            uniques.append(item)
        else:
            pass
    print(uniques)


uniquer([1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 6])