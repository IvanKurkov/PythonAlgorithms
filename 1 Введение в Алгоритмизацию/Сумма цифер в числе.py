# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

num = int(input('Введите целое трехзначное число: '))
a = num // 100
b = (num % 100) // 10
c = num % 10
comp = a * b * c
sum = a + b + c
print(f'Для числа {num} произведение цифр = {comp}\nсумма цифр = {sum}')