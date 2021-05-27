# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


# На ум приходит следующий алгоритм.
# 1) Создаем словарь для значений шестндцатиричной системы счисления, напримар 0:0, 1:1... 9:9, 10:А, 11:B...
# 2) Благодаря созданному словарю переводим число в десятичную систему и производим действие (складываем)
#  a) А2 = 10*16**1+2*16**0 = 162
#  b) C4F =  12*16**2+4*16**1+15*16**0 = 3151
#  c) a2+c4f = 3313
# 3) Переводим из 10чной в 16чную, по методу деления на 16,
# при этом остаток добавляется hexn.appendleft исходя из значений словаря.
from collections import deque

x = input("Введите первое 16ричное число:").upper()
y = input("Введите второе 16ричное число:").upper()

def sumhex(x,y):
    x = deque(x)
    y = deque(y)

    hexdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    spam = 0
    summ = 0
    while x:
        spam += (16 ** (len(x) - 1)) * hexdict[x.popleft()]
    summ += spam
    spam = 0
    while y:
        spam += (16 ** (len(y) - 1)) * hexdict[y.popleft()]
    summ += spam


    hexnum = deque()
    while True:
        if summ > 16:
            hexnum.appendleft(hexdict[summ % 16])
            summ //= 16
        else:
            hexnum.appendleft(hexdict[summ])
            break
    return list(hexnum)


def mulhex(x,y):
    x = deque(x)
    y = deque(y)

    hexdict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    spam = 0
    summ = 0
    while x:
        spam += (16 ** (len(x) - 1)) * hexdict[x.popleft()]
    summ += spam
    spam = 0
    while y:
        spam += (16 ** (len(y) - 1)) * hexdict[y.popleft()]
    summ *= spam


    hexnum = deque()
    while True:
        if summ > 16:
            hexnum.appendleft(hexdict[summ % 16])
            summ //= 16
        else:
            hexnum.appendleft(hexdict[summ])
            break
    return list(hexnum)

print(f"Сумма чисел = {sumhex(x,y)}")
print(f"Произведение чисел = {mulhex(x,y)}")