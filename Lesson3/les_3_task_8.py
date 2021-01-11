# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
import random

matrix = [[random.randint(0, 10) for _ in range(5)] for _ in range(4)]
print(matrix)
for i, row in enumerate(matrix):
    row_sum = 0
    for el in row:
        row_sum += el
    matrix[i].append(row_sum)
print(matrix)


