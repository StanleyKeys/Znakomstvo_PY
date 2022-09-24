"""
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
"""
def UserInput(inputText):                                   # Метод ввода текста
    userEnter = input(f"{inputText}")
    return userEnter                                  


def FillList(list):                                         # Метод заполнения списка
    userList = []                                                
    for i in list:
        userList.append(float(i))   
    return userList

userEnter = map(float, UserInput("Введите вещественные числа через пробел: ").split(" "))
newList = list(FillList(userEnter))
integerList = []
for i in newList:
    integerNumber = i - int(i)
    integerList.append(integerNumber)
    
differ = max(integerList) - min(integerList)                # Функция расчет максимального и минимального числа в списке  

answer = round(float(int(differ*1000)/1000), 2)                          #Перевод вещественного числа в целое с умножением 2-ух остатков и обратно для красоты
                                                            # round("число", "кол-во элементов после запятой") - функция округления числа
                                                            
print(f"Разница между максимальным и минимальным значением дробной части элементов: {answer}")
