# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры
sum = 1
prevNumber = 1
number = int(input('введите количество элементов > '))
for n in range(1, number):
    prevNumber = prevNumber / -2
    sum += prevNumber
print(f'sum: {sum}')
