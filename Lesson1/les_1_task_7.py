# Определить, является ли год, который ввел пользователь, високосным или не високосным
from calendar import isleap

year = int(input("введите год: "))
if isleap(year):
    print(f'{year} год високосный')
else:
    print(f'{year} не год високосный')
