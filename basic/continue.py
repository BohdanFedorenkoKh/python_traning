while True:
    s = input('введите что-нибуть :')
    if s == 'выход':
        break
    if len(s) < 3:
        print('слишком мало')
        continue
    print('Введена строка достаточной длины')