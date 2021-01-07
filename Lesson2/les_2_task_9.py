# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр
number = input('enter any number > ')
max_sum = 0
max_num = 0
for i in number:
    temp = 0
    for n in number:
        if n == i:
            temp += int(i)
    if temp > max_sum:
        max_sum = temp
        max_num = i
print(f'sum: {max_sum}; num: {max_num}')
