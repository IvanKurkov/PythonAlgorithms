
n = int(input("Введите количество элементов последовательности: "))
res = 0
el = 1
for i in range(0, n):
    res += el
    el *= -0.5
print(f"Сумма равна: {res}")