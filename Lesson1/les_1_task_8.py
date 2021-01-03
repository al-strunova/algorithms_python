# Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого)
first_number = int(input("введите первое число: "))
second_number = int(input("введите второе число: "))
third_number = int(input("введите третье число: "))
list_number = [first_number, second_number, third_number]
list_number.sort()
print(f'{list_number[1]} является средним')
