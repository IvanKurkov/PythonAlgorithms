# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
import random

mylist = [random.randint(-100, 100) for i in range(10)]
mylist = list(set(mylist))
print(mylist)
maxmin = mylist[0]
for i in mylist:
    if i > maxmin and i < 0:
        maxmin = i

print(maxmin)
