# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ.
import random

random_n = random.randint(0, 101)
for i in range(1, 11):
    number = int(input('your guess > '))
    if number == random_n:
        print(f'You won! The number of attempts: {i}')
        break
    elif number > random_n:
        print(f'The entered number is more than expected. You have {10 - i} more attempts')
    else:
        print(f'The entered number is less than expected. You have {10 - i} more attempts')
else:
    print(f'You did not win. There random number is {random_n}')
