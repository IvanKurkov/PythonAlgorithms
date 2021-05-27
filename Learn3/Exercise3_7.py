# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.


import random

mylist = [random.randint(-100, 100) for i in range(10)]

print(mylist)

#
# def myfn(list):
#     minlist = [0, 0]
#     min = list[0]
#     for i in list:
#         if min > i:
#             min = i
#             del minlist [0]
#             minlist.append(i)
#     return minlist
# print(myfn(mylist))
#
# def myfn(list):
#     minlist = [list[0], list[1]]
#     for i in list:
#         if minlist[0] > i :
#             del minlist [0]
#             minlist.append(i)
#     return minlist
# print(myfn(mylist))

minlist = []
while len(minlist) < 2:
    min = mylist[0]
    for i in mylist:
        if min > i:
            min = i
    mylist.remove(min)
    minlist.append(min)
print(minlist)
