# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#


# Первый — с помощью алгоритма «Решето Эратосфена».


def eratosfen(n):
    k = int(n ** 1.5 + 20)
    sieve = [i for i in range(k)]
    sieve[1] = 0
    for i in range(2, n + 1):
        if sieve[i] != 0:
            j = i * 2

            while j < k:
                sieve[j] = 0
                j += i
    return [i for i in sieve if i != 0][n - 1]


"""
"Exercise4_2.eratosfen(10)" 100 loops, best of 5: 7.5 usec per loop

"Exercise4_2.eratosfen(100)" 100 loops, best of 5: 175 usec per loop

"Exercise4_2.eratosfen(1000)" 100 loops, best of 5: 6.7 msec per loop

"Exercise4_2.eratosfen(10000)" 100 loops, best of 5: 300 msec per loop


"""

# Второй — без использования «Решета Эратосфена».

def myfn(n):
    k = int(n ** 1.5 + 20)
    if n == 1:
        return 2

    lst = [2]
    for i in range(3, k + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst[n - 1]


"""
"Exercise4_2.myfn(10)" 100 loops, best of 5: 8.35 usec per loop

"Exercise4_2.myfn(100)" 100 loops, best of 5: 249 usec per loop

"Exercise4_2.myfn(1000)" 100 loops, best of 5: 16.3 msec per loop

"Exercise4_2.myfn(10000)" 100 loops, best of 5: 1.42 sec per loop



"""

# Решето Эратосфена лучший алгоритм для данной задачи, т.к. для больших значений значительно снижает количество проверок
# путем отметания не подходящих значенй. В то время, как иные алгоритмы проверяющие перебором (до которых я додумался),
# даже при уточнении условий всеравно продолжают проверять слишеом много значений.
