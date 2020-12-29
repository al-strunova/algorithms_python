# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число,
# случайное вещественное число,
# случайный символ
import string
from random import randint, uniform, choice

case = input("Какие случайное значение вы хотите с генерировать? 'a' - случайное целое число;"
             " 'b' - случайное вещественное число, 'c' - случайный символ >>> ")
start = input("введите начало диапазона: ")
end = input("введите конец диапазона: ")
if case.lower() == 'a':
    print(f'случайное целое число: {randint(int(start), int(end))}')
elif case.lower() == 'b':
    print(f'случайное вещественное число: {(uniform(float(start), float(end))):.2f}')
elif case.lower() == 'c':
    print(f'случайный символ: {chr(randint(ord(start),ord(end)))}')
else:
    print(f'{case} не поддерживается в данном коде')

