# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

mylist = [random.randint(-100, 100) for i in range(10)]
mylist = list(set(mylist))
print(mylist)


def myfn(list):
    max = list[0]
    min = list[0]
    for i in list:
        if max < i:
            max = i
        if min > i:
            min = i
    indmax = list.index(max)
    indmin = list.index(min)
    print(f"Максимальное число: {max}, минимальное: {min}")
    summ = 0
    for x in list[indmax+1:indmin]:
        summ += x
    return f"Сумма элементов: {summ}"
print(myfn(mylist))