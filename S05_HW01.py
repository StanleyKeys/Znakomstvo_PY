"""
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
"""
userEnter = input("Введите желаемый текст: ")

userLength = len(userEnter)
userDel = userEnter.replace('абв', '', userLength)
print(userEnter)
print()
print(userDel)