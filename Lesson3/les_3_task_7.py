#  одномерном массиве целых чисел определить два наименьших элемента.
#  Они могут быть как равны между собой (оба минимальны), так и различаться
import random

array = [random.randint(0, 20) for _ in range(10)]
print(array)
min_value1 = min_value2 = array[0]
min_index1 = min_index2 = 0
for i, el in enumerate(array):
    if el < min_value1:
        min_value1 = el
    elif el < min_value2:
        min_value2 = el
print(min_value1, min_value2)
