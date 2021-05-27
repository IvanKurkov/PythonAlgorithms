# 1. Пользователь вводит данные о количестве предприятий,
# наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from collections import defaultdict

"""
# Создадим примерный набросок решения
cnt = int(input("Введите число компаний: "))


firms = []

for i in range(cnt):
    firms.append({"name": input("Введите название фирмы: "), "profit" : int(input("Введите прибыль: "))})
# Запросили количество фирм и заполнили данные
summ = 0

for dict in firms:
    summ += dict["profit"]

aver = summ/cnt
# Вычислили средний доход

low = []
hight = []


for dict in firms:
    if dict["profit"] > aver:
        hight.append(dict['name'])
    else:
        low.append(dict['name'])
# Разделили на выше и нииже среднего.
print(f"Фирмы с прибылью ниже среднего: {low}, фирмы с прибылью выше среднего: {hight}")

# Теперь смотрим как можно улучшить (или ухудшить =)) используя коллекции. 
"""

cnt = int(input("Введите число компаний: "))


firms = []

for i in range(cnt):
    firms.append({"name": input("Введите название фирмы: "), "profit" : int(input("Введите прибыль: "))})
# Запросили количество фирм и заполнили данные

summ = defaultdict(int)

for dict in firms:
    summ["profit"] += dict["profit"]
# Например можно использовать default dict для подсчета общей суммы заработка всех фирм
graddict = defaultdict(list)

for dict in firms:
    if dict["profit"] > summ["profit"]/cnt:
        graddict["Выше среднего"].append(dict["name"])
    else:
        graddict["Ниже среднего"].append(dict["name"])
# И для вывода результата
print(graddict)