class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function
    
    def __call__(self, *args, **kwargs):
        print(f'Call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)

@decorator_class
def display():
    print('This is a display function!!!')
    

@decorator_class
def display_info(name, age):
    print('display_info ran with arguments')

display_info('Bob', 30)
print('-.-.-.-.--.-.-.-')
display()

