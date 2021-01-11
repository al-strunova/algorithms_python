# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

array = [random.randint(0, 10) for _ in range(10)]
print(array)
min_value = max_value = array[0]
min_index = max_index = 0
for i, el in enumerate(array):
    if el < min_value:
        min_value = el
        min_index = i
    if el > max_value:
        max_value = el
        max_index = i
sum = 0
if min_index < max_index:
    for el in range(min_index + 1, max_index):
        sum += array[el]
if min_index > max_index:
    for el in range(max_index + 1, min_index):
        sum += array[el]
print(sum)
