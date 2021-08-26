import time 

def calc_prod():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

start_time = time.time()
prod = calc_prod()
end_time = time.time()
print(f'The result is {len(str(prod))} digits long.')
print(f'Took {end_time - start_time} seconds to calculate.')