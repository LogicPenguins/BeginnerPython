class doStuff():

    def __init__(self, word, person):
        self.word = word
        self.person = person
        
    def say_something(self):
        print(f'{self.person} would like to say {self.word}.')
    
doStuff_obj = doStuff("hello", "Xmexy")

doStuff_obj.say_something()