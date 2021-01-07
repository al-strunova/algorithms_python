# Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n — любое натуральное число
number = int(input('enter any natural number > '))
left_sum = 0
for i in range(1, number+1):
    left_sum += i
right_sum = number * (number + 1) / 2
print(f'(1 + 2+...+) {number} = {number} * ({number} +1) / 2 is {left_sum == right_sum}')
