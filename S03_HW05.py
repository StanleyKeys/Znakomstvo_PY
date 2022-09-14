"""
Задайте число. 
Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
"""

fib1 = fib2 = 1 
userNumber = int(input(" Введите число: "))
 

fibList = []
fibList.append(fib1)
fibList.append(fib2)
for i in range(2, userNumber):                          #Подсчет чисел Фибоначчи и заполнение списка
    fib1, fib2 = fib2, fib1 + fib2
    fibList.append(fib2)

if (i == userNumber-1):
    fib1 = fib2 = 1

negaFib = []
for i in range(-1, userNumber):                          # Cоздание отрицательного списка, и перевёрнутого.
    fib1, fib2 = fib2, fib1 - fib2
    negaFib.append(fib2)

print(fibList)                                           # Создание развернутого списка
reverseFib = []
for i in reversed(negaFib):
    reverseFib.append(i)

print(reverseFib)
print(f"Список Фибоначчи числа '{userNumber}' равна: {reverseFib + fibList}")

