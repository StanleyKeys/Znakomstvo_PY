"""
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

def UserInput(inputText):                                  # Метод ввода текста
    userEnter = input(f"{inputText}")
    return userEnter                                  

def FillList(list):                                        # Метод заполнения списка
    userList = []                                                
    for i in list:
        userList.append(int(i))   
    return userList

userEnter = UserInput("Введите числа через пробел: ")
newList = FillList(userEnter.split(" "))
print(f"Ваш список: {newList}")

reverseList = []                                            # Создание Разворотного списка
for i in reversed(newList):
    reverseList.append(i)

print(f"Список назад: {reverseList}")


summList = []

lengthList = len(newList)                                   # Деление длины списка пополам
if (lengthList%2 != 0):
    lengthList += 1

for i in range(0, lengthList//2):                           # Умножение чисел в двух списках и добавление каждого в новый список summList
    summList.append(newList[i]*reverseList[i])

print(f"Произведение пар чисел списка: {summList}")
