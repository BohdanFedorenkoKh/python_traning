number = 23
guess = int(input('введите целое число :'))

if guess == number:
    print('Поздравляю вы угадали ,') #начало нового блока 
    print('хотя и не выиграли никакого приза!')#конец нового блока 

elif guess < number:
    print('нет заданное число немного больше этого .')

else :
    print('нет заданное число немного меньше этого .')
