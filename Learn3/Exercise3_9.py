# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.



import random
n = 5 # Размер матрицы
arr = [[random.randint(0, 100) for i in range(n)] for j in range(n)]
for line in arr:
    for el in line:
        print(f"{el:>4}", end='')
    print()

print(f"*"*20)

list2 =[] #будущий список минимальных элементов

for line in list(zip(*arr[::-1])):  #Перевернули матрицу, теперь столбец изначальной равен строке нынешней, в строке ищем минимальный элемент.
    min = line[0]
    for i in line:
        if i < min:
            min = i
    list2.append(min)

print(f"Минимальные элементы стролбцов: {list2}")

max = list2[0]
for i in list2:  #Ищем максимальный элемент из минимальных
    if i > max:
        max = i
print(f"Максимальный элемент из минимальных элементов столбцов: {max}")


