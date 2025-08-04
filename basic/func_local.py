x = 50

def func(x):
    print('х равен,', x)
    x = 2
    print('замена локального х на', x)
func(x)
print('х по прежнему ', x)