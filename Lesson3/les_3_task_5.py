# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве
import random

array = [random.randint(-10, 10) for _ in range(10)]
print(array)
max_negative = array[0]
max_index = None
for i, el in enumerate(array):
    if el < 0 and el < max_negative:
        max_negative = el
        max_index = i
if max_index is None:
    print('В массиве нету отрицательных элементов')
else:
    print(f'{max_negative} максимальный отрицательный элемент который находится на {max_index} позиции')