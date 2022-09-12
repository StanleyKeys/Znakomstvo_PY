"""
Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

userEnter = int(input("Введите натуральное число N: "))

def Factor(y):                                      # Факторизация целых чисел
    list = []
    x = 2
    while x * x <= y:
        if y % x == 0:
            list.append(x)
            y //= x
        else:
            x += 1
    if y > 1:
        list.append(y)
    return list

print(f"Список простых множителей числа {userEnter} равен: ")
print(Factor(userEnter))
