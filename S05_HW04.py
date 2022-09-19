"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
"""
import os                                   # Код
clear = lambda: os.system('cls')            # очистки
clear()                                     # терминала
#====================================================      # Сжатие текста RLE
def ZipRLE(): 
    def RLE(line):
        result = []
        count = 0
        if len(line) == 1:
            result.append((1, line[0]))
            return result 
 
        for i in range(len(line)):
            count += 1
            if (i + 1) == len(line) or line[i] != line[i + 1]:
                result.append((count, line[i]))
                count = 0
        return result

    userInput = input("Введите строку:")
    result = RLE(userInput)
    rleList = []

    for amount, figure in result:
        temp = f"{amount}{figure}"
        rleList.append(temp)

    rleText = ("".join(rleList))
    print(rleText)
#========================================       Разжатие текста RLE
def UnzipRLE(): 
    def RLE():
        line = list(input("Введите строку: "))
        unzipList = []
        for i in range(len(line)):
            if (i % 2 == 0):
                count = line[i]
                val = line[i+1]
                count = int(count)
                res = count*val
                unzipList.append(res)
        print("".join(unzipList))
        return line
    #print("Расжатый текст получился: ")
    RLE()
#========================================                           # Сжатие файла zipInput.txt в файл zipOutput.txt
def ZipFileRLE():
    
    def RLE(line):
        result = []
        count = 0
        if len(line) == 1:
            result.append((1, line[0]))
            return result 
 
        for i in range(len(line)):
            count += 1
            if (i + 1) == len(line) or line[i] != line[i + 1]:
                result.append((count, line[i]))
                count = 0
        return result

    fileInput = input('Введите название файла, например "zipInput.txt":   ')
    if (fileInput == "") or (fileInput == " "):
        fileInput = "zipInput.txt"
    
    openFile = open(fileInput, "r")                                                       # Чтение файлов в данной папке
    lineList = openFile.readlines() 
    line = "".join(lineList)                                                   
    print(line)
    openFile.close()
    result = RLE(line)
    rleList = []

    for amount, figure in result:
        temp = f"{amount}{figure}"
        rleList.append(temp)

    rleText = ("".join(rleList))
    print(rleText)
    with open("zipOutput.txt", "w") as file:                                       # Запись в файл
        file.write(rleText)
    print('\nСжатие записано в файл "zipOutput.txt"')
#==============================================================    # Сжатие файла unzipInput.txt в файл unzipOutput.txt
def UnzipFIleRLE():   
    unzipList = []
    def RLE(a):
        line = list(a)
        for i in range(len(line)):
            if (i % 2 == 0):
                count = line[i]
                val = line[i+1]
                count = int(count)
                res = count*val
                unzipList.append(res)
        return line

    fileInput = input('Введите название файла, например "unzipInput.txt":   ')
    if (fileInput == "") or (fileInput == " "):
        fileInput = "unzipInput.txt"

    openFile = open(fileInput, "r")                                                       # Чтение файлов в данной папке    
    lineList = openFile.readlines() 
    line = "".join(lineList)                                                   
    openFile.close()
    RLE(line)
    line = "".join(unzipList)
    print(line)

    with open("unzipOutput.txt", "w") as file:                                       # Запись в файл
        file.write(line)
    print('\nРазжатие записано в файл "unzipOutput.txt"')
#==============================================================
userInput = int(input("Выберите действие RLE: \
                    \n1. Сжать текст\n2.Разжать текст \
                    \n3. Сжать текстовый файл \
                    \n4. Разжать текстовый файл\n"))
if (userInput == 1):
    ZipRLE()
if (userInput == 2):
    UnzipRLE()
if (userInput == 3):
    ZipFileRLE()
if (userInput == 4):
    UnzipFIleRLE()

