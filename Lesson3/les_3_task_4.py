# Определить, какое число в массиве встречается чаще всего
import random

array = [random.randint(1, 5) for _ in range(10)]
dic = {}
print(array)
max_count = 0
max_number = None
for i in array:
    if dic.get(i) is None:
        dic[i] = 1
    else:
        dic[i] += 1
    if dic[i] > max_count:
        max_count = dic[i]
        max_number = i
print(dic)
print(max_number)
