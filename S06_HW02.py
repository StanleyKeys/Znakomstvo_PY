"""Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""



def UserInput(inputText):                               # Метод ввода текста
    userEnter = input(f"{inputText}")
    return userEnter                                  

def FillList(list):                                        # Метод заполнения списка
    userList = []                                                
    for i in list:
        userList.append(int(i))   
    return userList

# userEnter = UserInput("Введите числа через пробел: ")
# splitList = userEnter.split(" ")

userEnter = map(int, UserInput("Введите числа через пробел: ").split())
newList = list(FillList(userEnter))

print(f"Ваш список: {newList}")

## Решение:

summ = 0
for id, val in enumerate(newList):                            
    if (id % 2 != 0):
        summ += val
    else:
        summ += 0

print(f"Сумма чисел в списке на нечетных позициях: {summ}")

## Ниже код можно разкоментить и будет другое решение.

# userInputElements = UserInput("Ввведите позиции элементов через пробел, которые нужно сложить: ")
# splitElements = userInputElements.split(" ")
# elementList = FillList(splitElements)

# summ = 0
# for i, i in enumerate(elementList):                           
#     number = newList[i]
#     summ += number

# print(f"Сумма чисел на указанных позицияхв списке: {summ}")
