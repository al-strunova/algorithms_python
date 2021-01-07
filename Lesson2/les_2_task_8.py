# Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры
number = input('enter any number > ')
number_to_count = input('enter a number to count > ')
cnt = 0
for i in number:
    if i == number_to_count:
        cnt += 1
print(cnt)
