alph = "abcdefghijklmnopqrstuvwxyz"
print("Вам нужно ввести 2 буквы английского алфавита в строчном виде.")
a = input("Введите первую букву: ")
b = input("Введите вторую букву: ")
x = int((alph.index(a)) + 1)
y = int((alph.index(b)) + 1)
c = abs(x - y) - 1
print(f"Позиция буквы {a}: {x},позиция буквы {b}: {y}, букв между между ними {c}")


####

# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Ведите две прописные буквы латинского алфавита:')
char1 = input('char1 = ')
char2 = input('char2 = ')

pos_char1 = ord(char1) - 64
pos_char2 = ord(char2) - 64
distance = abs(pos_char1 - pos_char2) - 1
print(f'Буква "{char1}" {pos_char1}-я в алфавите\n'
      f'Буква "{char2}" {pos_char2}-я в алфавите\n'
      f'Между буквами {distance} букв')
