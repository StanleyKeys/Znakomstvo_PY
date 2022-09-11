"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
userNumber = int(input(" Введите число: "))

def binaryCode(number):
    ans = ""
    while number > 0:
        ans = str(number % 2) + ans
        number = number // 2
    return ans

print(f"\nЧисло {userNumber} в двоичной системе: {binaryCode(userNumber)}")

print(f"\n{bin(userNumber)}")
