# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
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

    spam = list.index(min)
    list[list.index(max)] = min
    list[spam] = max
    return list


print(myfn(mylist))
