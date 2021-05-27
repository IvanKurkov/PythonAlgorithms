# 3.9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import timeit


def fn(n):
    # n - размер квадратной матрицы
    import random

    arr = [[random.randint(0, 100) for i in range(n)] for j in range(n)]

    list2 = []  # будущий список минимальных элементов

    for line in list(zip(*arr[::-1])):  # Перевернули матрицу, теперь столбец изначальной равен строке нынешней, в строке ищем минимальный элемент.
        min = line[0]
        for i in line:
            if i < min:
                min = i
        list2.append(min)

    max = list2[0]
    for i in list2:  # Ищем максимальный элемент из минимальных
        if i > max:
            max = i

    return list2


# "Exercise4_1.fn(10)" 1000 loops, best of 5: 99.1 usec per loop
# "Exercise4_1.fn(20)" 1000 loops, best of 5: 374  usec per loop
# "Exercise4_1.fn(40)" 1000 loops, best of 5: 1.62 msec  usec per loop


def fn2(n):
    import random

    arr = [[random.randint(0, 100) for i in range(n)] for j in range(n)]
    list2 = []  # будущий список минимальных элементов
    for j in range(len(arr[0])):
        min = arr[0][j]
        for i in range(len(arr)):
            if arr[i][j] < min:
                min = arr[i][j]
        list2.append(min)
    max = list2[0]
    for i in list2:  # Ищем максимальный элемент из минимальных
        if i > max:
            max = i

    return max

# "Exercise4_1.fn2(40)" 1000 loops, best of 5: 1.65 msec per loop
# "Exercise4_1.fn2(20)" 1000 loops, best of 5: 387 usec per loop
# "Exercise4_1.fn2(10)" 1000 loops, best of 5: 99.6 usec per loop

def fn3(n):


    import random

    arr = [[random.randint(0, 100) for i in range(n)] for j in range(n)]
    maxnum = max([min(line) for line in list(zip(*arr[::-1]))])

    return maxnum

# "Exercise4_1.fn3(10)" 1000 loops, best of 5: 94.1 usec per loop
# "Exercise4_1.fn3(20)" 1000 loops, best of 5: 354  usec per loop
# "Exercise4_1.fn3(40)" 1000 loops, best of 5: 1.43 msec  usec per loop


"""

Получить существенного ускорения процесса не получилось, однако 3 вариант гораздо интуитивно понятней и занимает меньше кода.

"""