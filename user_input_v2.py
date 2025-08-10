def reverse(text):
    return text[::-1]

def is_palindrome(text):
    # Кортеж всех запрещённых символов (пунктуация и пробелы)
    forbidden = ('!', '?', '.', ',', ':', ';', '-', ' ', "'", '"', '(', ')', '[', ']', '{', '}')
    
    # Удаляем запрещённые символы и приводим к нижнему регистру
    cleaned = ''.join(char.lower() for char in text if char not in forbidden)
    
    return cleaned == reverse(cleaned)

# Ввод от пользователя
something = input("Введите текст, чтобы проверить, является ли он палиндромом: ")

# Проверка
if is_palindrome(something):
    print("Да, это палиндром!")
else:
    print("Нет, это не палиндром.")
