# Найти максимальный элемент среди минимальных элементов столбцов матрицы
import random

matrix = [[random.randint(0, 10) for _ in range(5)] for _ in range(4)]
min_column_list = []
print(matrix)
for i, row in enumerate(matrix):
    min = row[0]
    for el in row:
        if el < min:
            min = el
    min_column_list.append(min)
print(min_column_list)
max = min_column_list[0]
for el in min_column_list:
    if el > max:
        max = el
print(max)


