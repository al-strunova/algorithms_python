# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.

# ******************** Первое решение - с помощью алгоритма «Решето Эратосфена» ********************
import cProfile


def solution1(n, pos):
    list_n = [i for i in range(n)]
    list_n[1] = 0
    for x in range(2, n):
        if list_n[x] != 0:
            j = x * 2
            while j < n:
                list_n[j] = 0
                j += x
    results = [i for i in list_n if i != 0]
    return results[pos]


# ******************** Второе решение — без использования «Решета Эратосфена» ********************
def solution2(n, pos):
    results = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0 and i != j:
                break
        else:
            results.append(i)
    return results[pos]

# ******************** Первое решение ********************
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.solution1(10)"
# 1000 loops, best of 5: 2.32 usec per loop    INPUT: 10
# 1000 loops, best of 5: 19.6 usec per loop    INPUT: 100
# 1000 loops, best of 5: 246  usec per loop    INPUT: 1000

# cProfile.run("solution1(1000)")
# 6 function calls in 0.000 seconds   INPUT: 10
# 6 function calls in 0.000 seconds   INPUT: 100
# 6 function calls in 0.001 seconds   INPUT: 1000


# ******************** Второе решение ********************
# python -m timeit -n 1000 -s "import les_4_task_2" "les_4_task_2.solution2(10)"
# 1000 loops, best of 5: 3.27 usec per loop    INPUT: 10
# 1000 loops, best of 5: 71.9 usec per loop    INPUT: 100
# 1000 loops, best of 5: 3.99 msec per loop    INPUT: 100

# cProfile.run("solution2(1000)")
# 8 function calls in 0.000 seconds, 4 0.000 0.000  0.000 0.000 {method 'append' of 'list' objects}     INPUT: 10
# 29 function calls in 0.000 seconds, 25 0.000 0.000 0.000 0.000 {method 'append' of 'list' objects}    INPUT: 100
# 172 function calls in 0.007 seconds, 168 0.000 0.000 0.000 0.000 {method 'append' of 'list' objects}  INPUT: 100

# ******************** Вывод ********************
# Первое решение является самым оптимальным
# так как оно самое быстрое вне зависимости от увеличения числа, плюс функция вызывается только один раз
