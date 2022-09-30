from collections import UserList
from queue import Empty
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.ttk import Combobox
from tkinter import ttk
import pandas as pd

window = Tk()
window.title("Телефонный Справочник")                       # Текст самого окна
window.geometry('1024x512')           
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)                               # Создание вкладок
tab2 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='Справочник')
tab_control.add(tab2, text='Поиск')   
tab_control.pack(expand=1, fill='both') 

def Save_Button_in_txt():
    infoGet = [surname.get(), name.get(), secondName.get(), phoneNumber.get(), country.get(), city.get(), birthDay.get(), birthMonth.get(), birthYear.get()] 
    with open('phoneDirectory.txt', 'a') as file:
        file.write(" ".join(infoGet) + '\n')
    Refresh_Scrollbar()

def Clear_Text_File():
    with open('phoneDirectory.txt', 'w') as file:
        file.write('')
    Refresh_Scrollbar()

def Refresh_Scrollbar():
    scrollTextBar.delete(1.0, END)                                            
    scrollTextBar.insert(INSERT, open('phoneDirectory.txt').read())

#===========================================================================================
coincidence = []
def Search_Button():
    infoGet = [surname.get(), name.get(), secondName.get(), phoneNumber.get(), country.get(), city.get(), birthDay.get(), birthMonth.get(), birthYear.get()] 
    lines = Read2List('phoneDirectory.txt')
    
    for val in lines:
        tempList = val.split()
        similarity = list(set(tempList) & set(infoGet))
        if (len(similarity) > 0):
            for id, val in enumerate(tempList):
                if (id == 0) or (id == 1) or (id == 2):
                    tempString = " ".join(tempList)
            coincidence.append(tempString)
     
    combo['values'] = coincidence
    combo.current(0)

#===========================================================================================

def Show_Info_Button():
    userValue = combo.get()
    with open('phoneDirectory.txt') as file:
        for line in file:
            if userValue in line:
                tempList = line.split()

    while len(tempList) !=7:
        tempList.append(" ") 

    for id, val in enumerate(tempList):
        if (id == 0):
            labelShowSurname = Label(tab2, text = "Фамилия: " + val + "        ", font=("Arial Bold", 12)) 
            labelShowSurname.place(x=600,y=30)
            if val == '':
                labelShowSurname.configure(text="Фамилия: ")
        if (id == 1):
            labelShowName = Label(tab2, text = "Имя: " + val + "      ", font=("Arial Bold", 12)) 
            labelShowName.place(x=630,y=70)
            if val == '':
                labelShowSurname.configure(text="Имя: ")
        if (id == 2):
            labelShowSecondName = Label(tab2, text = "Отчество: " + val + "        ", font=("Arial Bold", 12)) 
            labelShowSecondName.place(x=600,y=110)
            if val == '':
                labelShowSurname.configure(text="Отчество: ")
        if (id == 3):   
            labelShowPhone = Label(tab2, text = "Телефон: " + val + "         ", font=("Arial Bold", 12))
            labelShowPhone.place(x=604,y=150)
            if val == '':
                labelShowSurname.configure(text="Телефон: ")
        if (id == 4):
            labelShowCountry = Label(tab2, text = "Страна: "+ val + "       ", font=("Arial Bold", 12))
            labelShowCountry.place(x=613,y=190)
            if val == '':
                labelShowSurname.configure(text="Страна: ")
        if (id == 5):
            labelShowCity = Label(tab2, text = "Город: "+ val + "       ", font=("Arial Bold", 12)) 
            labelShowCity.place(x=619,y=230)
            if val == '':
                labelShowSurname.configure(text="Город: ")
        if (id == 6):
            labelShowBirthDate = Label(tab2, text = "Д/Р: " + val  + "        ", font=("Arial Bold", 12)) 
            labelShowBirthDate.place(x=633,y=270)
            if val == '':
                labelShowSurname.configure(text="Д/Р: ")

#============================================================================================     

def Convert_Excel_Button():
    surnameList = []
    nameList = []
    secNameList = []
    phoneList = []
    countryList = []
    cityList = []
    with open('phoneDirectory.txt') as file:
        for line in file:
            tempList = line.split()
            for id, val in enumerate(tempList):
                if (id == 0):
                    surnameList.append(val)
                if id == 1:
                    nameList.append(val)
                if id == 2:
                    secNameList.append(val)
                if id == 3:
                    phoneList.append(val)
                if id == 4:
                    countryList.append(val)
                if id == 5:
                    cityList.append(val)
        dictFull = {"Фамилия" : surnameList, "Имя" : nameList, "Отчество" : secNameList, "Телефон" : phoneList, "Страна" : countryList, "Город" : cityList}
        convertFile = pd.DataFrame.from_dict(dictFull,'index').reset_index()
        convertFile.to_excel("phoneList.xlsx", index=False)
        labelSuccess = Label(tab1, text = 'Ваш справочник успешно сохранен в "phoneList.xlsx"', font=("Arial Bold", 10))
        labelSuccess.place(x=105,y=300)

#===========================================================================================
def Read2List(file):
    file = open(file, 'r')
    # читаем все строки и удаляем переводы строк
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    file.close()
    return lines


#------------------------------------------------------------------------------     # Создание кнопок
saveButton = Button(tab1, text="Добавить запись", command=Save_Button_in_txt)
saveButton.place(x=5, y=250)
clearTextButton = Button(tab1, text="Очистить список", command=Clear_Text_File)
clearTextButton.place(x=300, y=250)
searchButton = Button(tab2, text="Поиск", command=Search_Button)
searchButton.place(x=10, y=200)
showInfoButton = Button(tab2, text="Показать", command=Show_Info_Button)
showInfoButton.place(x=280, y=200)
convertExcelButton = Button(tab1, text="Экспорт в Excel", command=Convert_Excel_Button)
convertExcelButton.place(x=5, y=300)
#------------------------------------------------------------------------------

headerText = Label(window, text = "Телефонный справочник", font=("Arial Bold", 12))
headerText.place(x=700, y=1)
scrollTextBar = scrolledtext.ScrolledText(tab1, width=50, height=28)                   # Большое окно со списком
scrollTextBar.place(x=600,y=30)
scrollTextBar.insert(INSERT, open('phoneDirectory.txt').read())

labelSurname = Label(window, text = "Фамилия", font=("Arial Bold", 10)) 
labelSurname.place(x=15,y=50)
surname = Entry(window, width=15)
surname.place(x=5,y=75)

labelName = Label(window, text = "Имя", font=("Arial Bold", 10)) 
labelName.place(x=135,y=50)
name = Entry(window, width=15)
name.place(x=105, y=75)

labelSecondName = Label(window, text = "Отчество", font=("Arial Bold", 10)) 
labelSecondName.place(x=220,y=50)
secondName = Entry(window, width=15)
secondName.place(x=205,y=75)

labelPhoneNumber = Label(window, text = "Телефон", font=("Arial Bold", 10)) 
labelPhoneNumber.place(x=15,y=100)
phoneNumber = Entry(window, width=15)
phoneNumber.place(x=5,y=125)

labelCountry = Label(window, text = "Страна", font=("Arial Bold", 10)) 
labelCountry.place(x=120,y=100)
country = Entry(window, width=15)
country.place(x=105,y=125)
labelCity = Label(window, text = "Город", font=("Arial Bold", 10)) 
labelCity.place(x=225,y=100)
city = Entry(window, width=15)
city.place(x=205,y=125)

labelBirthDate = Label(window, text = "Дата рождения", font=("Arial Bold", 10)) 
labelBirthDate.place(x=78,y=150)
labelBirthDay = Label(window, text = "День: ", font=("Arial Bold", 10)) 
labelBirthDay.place(x=1,y=175)
birthDay = Entry(window, width=4)
birthDay.place(x=43,y=178)
labelBirthMonth = Label(window, text = "Месяц: ", font=("Arial Bold", 10)) 
labelBirthMonth.place(x=75,y=175)
birthMonth = Entry(window, width=4)
birthMonth.place(x=128,y=178)
labelBirthYear = Label(window, text = "Год: ", font=("Arial Bold", 10)) 
labelBirthYear.place(x=160,y=175)
birthYear = Entry(window, width=5)
birthYear.place(x=195,y=178)
searchLabel = Label(tab2, text="Введите параметры для поиска", font=("Arial Bold", 13))
searchLabel.place(x=25,y=5)
#-------------------------------------------------------------------------------------   # Создание выпадающего списка
combo = Combobox(tab2, width=30, state="readonly")  
combo.place(x=65,y=203)
#-------------------------------------------------------------------------------------

resLabel = Label(tab2, text=" ", font=("Arial Bold", 13))
resLabel.place(x=700,y=50)

window.mainloop()