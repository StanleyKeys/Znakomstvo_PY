""" Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных пользователем через пробел позициях."""

n = int(input(" Введите число: "))                                  # Заполнение списка числами от -N до N
list = []
for i in range(-n, n+1):
    list.append(i)                                                  # end

print(f"Ваш список от -{n} до {n} = {list}")


listElement = input(" Введите позицию элемента через пробел: ")
splitList = listElement.split(" ")                                  #Создание нового списка и разделение старого

positionElement = []                                                #Создание списка из введеных пользователем элементов
for i in splitList:
    positionElement.append(int(i))

sum = 0
number = 0

print("Выбранные элементы списка: ")

for i, i in enumerate(positionElement):                             #Суммирование выбранных элементов списка
    number = list[i]
    sum += number
    print(number)
   
print(f"Сумма выбранных элементов в списке равна: {sum}")
