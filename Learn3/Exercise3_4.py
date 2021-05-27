# 4. Определить, какое число в массиве встречается чаще всего.
import random

mylist = [random.randint(0, 10) for i in range(15)]
print(mylist)

def myfn(mylist):
    maxcount = 0
    maxnum = 0
    for i in mylist:
        if mylist.count(i) > maxcount:
            maxcount = mylist.count(i)
            maxnum = i
    if maxcount == 1:
        return f"Все элементы уникальны"
    return maxnum

print(myfn(mylist))