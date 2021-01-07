# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random

array = [random.randint(1, 20) for _ in range(10)]
print(array)
min_index = max_index = 0
min_value = max_value = array[0]
for i, el in enumerate(array):
    if el < min_value:
        min_value = el
        min_index = i
    if el > max_value:
        max_value = el
        max_index = i
array[min_index], array[max_index] = max_value, min_value
print(array)
