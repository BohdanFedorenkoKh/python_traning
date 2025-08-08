class Person:
    def __init__(self,name):
        self.name = name

    def say_hi(self):
        print('Привет! меня зовут', self.name)

p = Person('Bohdan')
p.say_hi()

# Предыдущие 2 строки можно
# Person('Bohdan').say_hi()
