# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
#   заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
#   Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
import random


def bubble_reverse_sort(array):
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - 1 - i):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


a = [i for i in range(-100, 100)]
random.shuffle(a)
print(a)
bubble_reverse_sort(a)
print(a)
