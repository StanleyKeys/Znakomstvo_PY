"""
Задайте число. 
Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
"""

fib1 = fib2 = 1
 
userNumber = int(input(" Введите число: "))
 

fibbList = []
fibbList.append(fib1)
fibbList.append(fib2)
for i in range(2, userNumber):                          #Подсчет чисел Фибоначчи и заполнение списка
    fib1, fib2 = fib2, fib1 + fib2
    
    fibbList.append(fib2)
    #print(fib2, end=' ')
print(fibbList)

negativefibb = []

for i in reversed(fibbList):                            # Cоздание отрицательного списка, и перевёрнутого.
    negativefibb.append(i*-1)

print(negativefibb)

print(f"Список Фибоначчи числа '{userNumber}' равна: {negativefibb+[0]+fibbList}")

