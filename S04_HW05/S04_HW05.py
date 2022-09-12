"""
Даны два файла, в каждом из которых находится запись многочлена. 
Задача - сформировать файл, содержащий сумму многочленов.
"""
## !!! Текстовые файлы должны находится в той папке откуда запускается терминал !!!##

f1 = input('Введите название файла, например "input.txt":   ')
if (f1 == "") or (f1 == " "):
    f1 = "input.txt"

f2 = input('Введите название второго файла, например "inputTwo.txt":   ')
if (f2 == "") or (f2 == " "):
    f2 = "inputTwo.txt"

def ReadLine(file):                                                         # Чтение файлов в данной папке и добавление переменных в список
    a = open(file,"r")
    line = a.readlines()                                                    
    fileList = list(line[0])
    a.close()
    return fileList
    

def DeleteSymbols(listDel):                                                 # Удаление символа умножения
    for i in range(0,len(listDel)-1):
        if (listDel[i] == '*'):
            listDel.pop(i)
    listDel = ("".join(listDel))                                            # Соединение списка в строку
    return listDel


equation = f"{DeleteSymbols(ReadLine(f1))} + {DeleteSymbols(ReadLine(f2))} = 0" # Cамо уравнение

with open("output.txt", "w") as file:                                       # Запись уравнения в файл
    file.write(equation)


print('\nУравнение записано в файл "output.txt"')
print(f"\n\nВаше уравнение: {equation}")

