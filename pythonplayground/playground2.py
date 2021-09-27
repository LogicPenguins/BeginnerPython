import time

def my_timer(original_func):

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        time.sleep(1)
        t2 = time.time() - t1
        print(f'{original_func.__name__} ran in {t2} seconds.')
        return result
    return wrapper


@my_timer
def display_info(name, age):
    print(f'Name is {name}, age is {age}.')



display_info('Bob', 40)