class ScoolMembr:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создан ScoolMembr: {0}'.format(self.name))

    def tell(self):
        '''Вывести информацию.'''
        print('Имя:"{0}" Возраст:"{1}"'.format(self.name, self.age), end ="")

class Teacher(ScoolMembr):
    '''Представляет преподавателя.'''
    def __init__(self, name, age , salary):
        ScoolMembr.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    def tell(self):
        ScoolMembr.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(ScoolMembr):
    def __init__(self, name ,age , marks):
        ScoolMembr.__init__(self, age, name)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    
    def tell(self):
        ScoolMembr.tell(self)
        print('Оценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Bohdan', 25, 75)

print() # печатает пустую строку

members = [t, s]
for member in members:
    member.tell() # работает как для преподавателя, так и для студента