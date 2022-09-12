"""
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""
import random
 
userEnter = int(input(f"Введите число N: "))
 
L, Exists = list(), list()
 
for i in range(userEnter):
    L.append(random.randint(0, userEnter))
    Exists.append(True)
 
print('Изначальный список:')
print(L)
 
for i in range(userEnter):
    if Exists[i]:
        for j in range(i + 1, userEnter):
            if L[j] == L[i]:
                Exists[j] = False
 

originList = list()
for i in range(userEnter):
    if Exists[i]:
        originList.append(i)
print(f"\nСписок оригинальных элементов: {originList}")