""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях."""

from typing import List

n = int(input(" Введите число: "))                                  # Заполнение списка числами от -N до N
list = []
for i in range(-n, n+1):
    list.append(i)                                                  # end

print(f"Ваш список от -{n} до {n} = {list}")

# listElement = input(" Введите позицию элемента через пробел: ")
# splitList = listElement.split(" ")                                  #Создание нового списка и разделение старого

# positionElement = []                                                #Создание списка из введеных пользователем элементов
# for i in splitList:
#     positionElement.append(int(i))

listElement = map(int, input(" Введите позицию элемента через пробел: ").split(" "))

multip = 1
number = 0

print("Выбранные элементы списка: ")

for i, i in enumerate(listElement):                             #Произведение выбранных элементов списка
    number = list[i]
    multip *= number
    print(number)
   
print(f"Произведение выбранных элементов в списке равна: {multip}")