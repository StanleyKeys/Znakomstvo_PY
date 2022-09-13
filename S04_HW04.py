"""
Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
"""
import random
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }

k = input("Введите натуральную степень k: ")
l = input("Введите натуральную степень l, если она есть: ")

def DegreeCheck(degree):
    if (degree != ""):                                       # Проверка полученного числа k, l на положительную степень
        degree = int(degree)
        if (degree < 2):
            degree = ""
    return degree


a = 0
def RandomNumbers(d):                               # Заполение уравнения случайными числами
    d = random.randint(2, 100)
    return d

def DegreePrint(a: int):                                 # Метод написания степени у многочлена
    degrees = ""
    temp = str(a)
    for char in temp:
        degrees += indexes[char] or ""
    return degrees


print(f"Уравнение: {RandomNumbers(a)}x{DegreePrint(DegreeCheck(k))} + {RandomNumbers(a)}y{DegreePrint(DegreeCheck(l))} - {RandomNumbers(a)} = 0")
