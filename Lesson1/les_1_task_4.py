# Пользователь вводит две буквы. Определить,
# на каких местах алфавита они стоят,
# и сколько между ними находится букв
first = ord(input("введите первую букву: "))
second = ord(input("введите вторую букву: "))
print(f'Позиция первой буквы: {first - ord("a") + 1}')
print(f'Позиция второй буквы: {first - ord("a") + 1}')
print(f'Между буквами {abs(first - second) - 1} символов')

