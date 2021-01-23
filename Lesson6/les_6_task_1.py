# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
import sys


# ************** версия и разрядность ОС и Python **************

# Python version: v3.8.5 , Platform: MaOS 64-bit

# ************** функция сложения всех затрат памяти **************

def count_size(x, level=0):
    size = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                size += sys.getsizeof(key)
                size += sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                size += sys.getsizeof(item)
    return size


# *************** Задача 1 **************

# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
bit_and = 5 & 6
bit_or = 5 | 6
bit_xor = 5 ^ 6
bit_left = 5 << 2
bit_right = 5 >> 2

print(f'{5} & {6} = {bit_and}')
print(f'{5} | {6} = {bit_or}')
print(f'{5} ^ {6} = {bit_xor}')
print(f'{5} << {2} = {bit_left}')
print(f'{5} >> {2} = {bit_right}')

sum_ = 0
var_lst = (bit_and, bit_or, bit_xor, bit_left, bit_right)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 140 байт памяти
# Пять переменных типа инт
# type=<class 'int'>, size=28, object=4
# type=<class 'int'>, size=28, object=7
# type=<class 'int'>, size=28, object=3
# type=<class 'int'>, size=28, object=20
# type=<class 'int'>, size=28, object=1

# *************** Задача 2 **************

# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)
even = 0
odd = 0
number = '34560'
for position in range(len(number)):
    if int(number[position]) % 2 != 0:
        odd += 1
    else:
        even += 1
print(f'в натуральном числе "{number}": {even} четных и {odd} нечетных чисел')

sum_ = 0
var_lst = (even, odd, number, position)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 138 байт памяти
# Одна переменная типа str, три переменных int
# type=<class 'int'>, size=28, object=3
# type=<class 'int'>, size=28, object=2
# type=<class 'str'>, size=54, object=34560
# type=<class 'int'>, size=28, object=4

# *************** Задача 3 **************

# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр
number = '12343213211'
max_sum = 0
max_num = 0
for i in number:
    temp = 0
    for n in number:
        if n == i:
            temp += int(i)
    if temp > max_sum:
        max_sum = temp
        max_num = i
print(f'sum: {max_sum}; num: {max_num}')

sum_ = 0
var_lst = (number, max_sum, max_num, i, temp, n)
for i in var_lst:
    sum_ += count_size(i)
print(f'Под переменные задействованно {sum_} байт памяти')

# Под переменные задействованно 266 байт памяти
# Четыре переменных типа str, две переменных int
# type=<class 'str'>, size=60, object=12343213211
# type=<class 'int'>, size=28, object=9
# type=<class 'str'>, size=50, object=3
# type=<class 'str'>, size=50, object=1
# type=<class 'int'>, size=28, object=4
# type=<class 'str'>, size=50, object=1
