number = 23
runing = True

while runing:
    guess = int (input('Введите целое число : '))

    if guess == number:
        print('Поздравляю вы угадали')
        runing = False # это останавливает цикл while
    elif guess < number:
        print('Нет , загаданное число немного больше этого')
    else:
        print('Нет,загаданное число немного меньше этого')

else:
    print('цикл while закончен')