# 'ab' - сокращение от 'a'ddres 'b'ook

ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto' : 'matz@ruby-lang.org',
    'Spammer' : 'spammer@hotnail.com',
}

print ("Адресс Swarppo'a", ab['Swaroop'])

#удаление парв ключ-значение 
del ab['Spammer']
print('\nВ адресной книге {0} контанта\n'.format(len(ab)))

for name, adress in ab.items():
    print('Контакт {0} с адресом  {1}'.format(name,adress))

ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])