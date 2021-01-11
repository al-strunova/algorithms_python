# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.
import cProfile


# ******************** Первое решение ********************
def solution1(n):
    if len(n) == 1:
        return n
    else:
        return solution1(n[1:]) + n[0]


# ******************** Второе решение ********************
def solution2(n):
    return n[::-1]


# ******************** Третье решение ********************
def solution3(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    return result

# ******************** Первое решение ********************
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.solution1('12345')"
# 1000 loops, best of 5: 1.26 usec per loop    INPUT: '12345'
# 1000 loops, best of 5: 2.89 usec per loop    INPUT: '12345678901'
# 1000 loops, best of 5: 5.61 usec per loop    INPUT: '123456789012345678901'
# 1000 loops, best of 5: 8.22 usec per loop    INPUT: '1234567890123456789012345678901'

# cProfile.run("solution1('12345')")
# 5/1     0.000    0.000    0.000    0.000 les_4_task_1.py:7(solution1)   INPUT: '12345'
# 11/1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(solution1)   INPUT: '12345678901'
# 21/1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(solution1)   INPUT: '123456789012345678901'
# 31/1    0.000    0.000    0.000    0.000 les_4_task_1.py:7(solution1)   INPUT: '1234567890123456789012345678901'

# ******************** Второе решение ********************
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.solution2('12345')"
# 1000 loops, best of 5: 211 nsec per loop    INPUT: '12345'
# 1000 loops, best of 5: 222 nsec per loop    INPUT: '12345678901'
# 1000 loops, best of 5: 294 nsec per loop    INPUT: '123456789012345678901'
# 1000 loops, best of 5: 322 nsec per loop    INPUT: '1234567890123456789012345678901'


# cProfile.run("solution2('12345678901')")
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(solution2)    INPUT: '12345'
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(solution2)    INPUT: '12345678901'
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(solution2)    INPUT: '123456789012345678901'
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:15(solution2)    INPUT: '1234567890123456789012345678901'

# ******************** Третье решение ********************
# python -m timeit -n 1000 -s "import les_4_task_1" "les_4_task_1.solution3(12345)"
# 1000 loops, best of 5: 944 nsec per loop     INPUT: 12345
# 1000 loops, best of 5: 1.7 usec per loop     INPUT: 12345678901
# 1000 loops, best of 5: 4.04 usec per loop    INPUT: 123456789012345678901
# 1000 loops, best of 5: 6.56 usec per loop    INPUT: 1234567890123456789012345678901

# cProfile.run("solution3(12345678901)")
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(solution3)    INPUT: '12345'
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(solution3)    INPUT: '12345678901'
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(solution3)    INPUT: '123456789012345678901'
# 1    0.000    0.000    0.000    0.000 les_4_task_1.py:20(solution3)    INPUT: '1234567890123456789012345678901'


# Второе решение является самым оптимальным
# так как оно самое быстрое вне зависимости от увеличения числа плюс функция вызывается только один раз