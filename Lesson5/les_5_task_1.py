# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего
from collections import ChainMap

companies = ChainMap()
nbr = int(input('Введите количество предприятий: '))
sum_profit = 0
for i in range(nbr):
    name = input(f"Введите название {i+1}й компании: ")
    profit = float(input('Введите прибыль за 1й квартал: ')) + float(input('Введите прибыль за 2й квартал: ')) + float(
        input('Введите прибыль за 3й квартал: ')) + float(input('Введите прибыль за 4й квартал: '))
    companies = companies.new_child({name: profit})
    sum_profit += profit
average_profit = sum_profit / nbr
print(f'Средняя прибыль для всех компаний составила: {average_profit}')
comp_dict_high = [k for k, v in companies.items() if v >= average_profit]
print(f'Прибыль выше среднего у {len(comp_dict_high)} компаний: {comp_dict_high}')
comp_dict_low = [k for k, v in companies.items() if v < average_profit]
print(f'Прибыль ниже среднего у {len(comp_dict_low)} компаний: {comp_dict_low}')

