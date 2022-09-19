"""
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""
"""

from random import randint, random
import sys
from fileinput import close
import os                                   # Код
clear = lambda: os.system('cls')            # очистки
clear()                                     # терминала
#===========================================================================
print('                 Добро пожаловать в игру "Конфетная Лихорадка"!')
print('-На столе лежат 2021 конфета. Игроки ходят по очереди.- ')
print('-Можно брать не больше 28 конфет за один ход! Побеждает ТОТ, кто забирает последнюю конфету!-')
entrance = input("\nНажмите любую клавишу для продолжения ")
candyCount = 2021
clear()
#============================================================================
def InputCheck(playerInput):                                                # Модуль проверки на ввод пользователя
    while True:
        playerInput = input("Введите количество конфет: ")
        if (playerInput == 'exit'):
            print("Игра была Прервана!")
            sys.exit()

        if (int(playerInput) > 28):
            print("Можно взять НЕ более 28 конфет за один ход!")
        if (candyCount - int(playerInput) < 0):
            print("На столе осталось меньше конфет, чем ты хочешь взять!")
        if (int(playerInput) == 0):
            print("А нет уж! Надо взять хотя бы одну конфетку!")

        if (0 < int(playerInput) <= 28) and (candyCount - int(playerInput) >= 0):
            break  
    return playerInput
#============================================================================
def PvPMode():                                                                # Player Vs Player Mode - режим игры против "Игрок против Игрока"
    candyCount = 2021   
    lotChoice = randint(1, 2)
        
    playerOneName = "Игрок 1"
    playerTwoName = "Игрок 2"
    input("Выбираем кто будет первый ходить: ")                             # Жребий
    if (lotChoice == 1):
        input(f"Выпало число {lotChoice}. Ходит {playerOneName}")
    if (lotChoice == 2):
        input(f"Выпало число {lotChoice}. Ходит {playerTwoName}")

    while candyCount >= 0:
        player1 = ""
        player2 = ""
        
        if (lotChoice == 1):                                            # Ход игрока 1
            print("Ход игрока 1: ")
            candyCount -= int(InputCheck(player1))
            clear()
            print(f"Осталось: {candyCount} конфет")
            lotChoice = 2
            if (candyCount == 0):
                print("Поздравляю! Победил Игрок 1!")
                break
            
        
        if (lotChoice == 2):                                            # # Ход игрока 2        
            print("Ход игрока 2: ")
            candyCount -= int(InputCheck(player2))
            clear()
            print(f"Осталось: {candyCount} конфет")
            lotChoice = 1
            if (candyCount == 0):
                print("Поздравляю! Победил Игрок 2!")
                break               
    return candyCount
#=========================================================================
def PvCMode():                                                              # Player Vs Computer Mode - режим игры против "Игрок против Компьютера"
    candyCount = 2021
    lotChoice = randint(1, 2)
        
    playerOneName = "Игрок 1"
    computerName = "Компьютер"
    input("Выбираем кто будет первый ходить: ")
    if (lotChoice == 1):
        input(f"Выпало число {lotChoice}. Ходит {playerOneName}")
    if (lotChoice == 2):
        input(f"Выпало число {lotChoice}. Ходит {computerName}")
   
    while candyCount >= 0:
        player1 = ""
        
        if (lotChoice == 1):                                            # Ход игрока
            playerTurn = int(InputCheck(player1))
            clear()
            print(f"Ваш ход: {playerTurn}")
            candyCount -= playerTurn
            lotChoice = 2
            if (candyCount == 0):
                print("Поздравляю! Вы победили!")
                break

        if (lotChoice == 2):                                            # Ход компьютера
            compTurn = randint(1, 28) 
            if (candyCount - compTurn < 0):
                compTurn = candyCount
            print(f"Ход компьютера: {compTurn} ")
            candyCount -= compTurn
            print(f"Осталось: {candyCount} конфет\n")
            lotChoice = 1
            if (candyCount == 0):
                print("Победил Компьютер! Нечего было покупать i9-12900K")
                break    
    return candyCount
#===========================================================================
def HardMode():                                                             # Hard Mode - режим игры против умного компьютера
    candyCount = 200
    lotChoice = randint(1, 2)
    playerOneName = "Игрок 1"
    computerName = "Компьютер"

    input("Выбираем кто будет первый ходить: ")
    if (lotChoice == 1):
        input(f"Выпало число {lotChoice}. Ходит {playerOneName}")
    if (lotChoice == 2):
        input(f"Выпало число {lotChoice}. Ходит {computerName}")

    while candyCount >= 0:
        player1 = ""

        if (lotChoice == 1):
            playerTurn = int(InputCheck(player1))
            #clear()
            print(f"Ваш ход: {playerTurn}")
            candyCount -= playerTurn
            lotChoice = 2
            if (candyCount == 0):
                print("Поздравляю! Вы победили!\nПора изобретать Джарвиса")
                break
        
        if (lotChoice == 2):
            compTurn = randint(1, 28)

            if (candyCount - compTurn > 29): 
                candyCount = candyCount - compTurn
                print(f"Ход компьютера: {compTurn} ")
                lotChoice = 1
            elif (candyCount <= 28):
                compTurn = candyCount
                print(f"Ход компьютера: {compTurn} ")
                candyCount -= compTurn
                lotChoice = 1
                if (candyCount == 0):
                    print("Победил Компьютер!\nP.S. он использовал Cheat Engine :)")
                    break  

            elif (candyCount - 28 <= 29):
                compTurn = candyCount - 27
                temp = candyCount - 27
                temp = 27 - temp
                candyCount = candyCount - 27 + temp + 1
                compTurn = 1
                print(f"Ход компьютера: {compTurn} ")
                lotChoice = 1
            print(f"Осталось: {candyCount} конфет\n")
            if (candyCount == 0):
                print("Победил Компьютер!\nПланета будет захвачена ИИ!")
                break
    return candyCount
#=======================================================================
modeChoice = input("Есть три режима игры: \
                  \n1. Игрок против Игрока \
                  \n2. Игрок против Компьютера \
                  \n3. Игрок против Умного Компьютера \
                  \nКакой режим вы хотите выбрать?:   ")
                                                                        # Модуль выбора режима игры
if (int(modeChoice) == 1):
    PvPMode()
if (int(modeChoice) == 2):
    PvCMode()
if (int(modeChoice) == 3):
    HardMode()
#=======================================================================