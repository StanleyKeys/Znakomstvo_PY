from collections import UserList
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.ttk import Combobox


def Add_Interface(): 
    
    def Save_Button_in_txt():  
        with open('phoneDirectory.txt', 'a') as file:
            file.write(f'{surname.get()} ' + f'{name.get()} ' + f'{secondName.get()} ' + f'{phoneNumber.get()} ' + f'{country.get()} ' + f'{city.get()} ' + f'{birthDay.get()}.{birthMonth.get()}.{birthYear.get()} \n')
        Refresh_Scrollbar()

    def Clear_Text_File():
        with open('phoneDirectory.txt', 'w') as file:
            file.write(' ')
        Refresh_Scrollbar()

    def Refresh_Scrollbar():
        scrollTextBar.delete(1.0, END)                                            
        scrollTextBar.insert(INSERT, open('phoneDirectory.txt').read())

    global saveButton, clearTextButton, headerText, scrollTextBar, labelSurname, surname, labelName, name, labelSecondName, secondName
    global labelPhoneNumber, phoneNumber, labelCountry, country, labelCity, city
    global labelBirthDate, labelBirthDay, birthDay, labelBirthMonth, birthMonth, labelBirthYear, birthYear
    global searchLabel
    saveButton = Button(window, text="Сохранить", command=Save_Button_in_txt)
    saveButton.place(x=5, y=250)
    clearTextButton = Button(window, text="Очистить список", command=Clear_Text_File)
    clearTextButton.place(x=300, y=250)


    headerText = Label(window, text = "Телефонный справочник", font=("Arial Bold", 12))
    headerText.place(x=700, y=1)
    scrollTextBar = scrolledtext.ScrolledText(window, width=50, height=28, state='disabled')                   # Большое окно со списком
    scrollTextBar.place(x=600,y=30)
    # print(open('phoneDirectory.txt').read())
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
    searchLabel = Label(window, text = "Введите данные", font=("Arial Bold", 16))
    searchLabel.place(x=10, y=10)

def Search_Interface():
    
    # combo = Combobox(window)
    # combo['values'] = (1, 2, 3, 4, 5, "Текст")  
    # combo.current(1)  # установите вариант по умолчанию  
    # combo.grid(column=0, row=0)
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
    
    searchLabel = Label(window, text = "Введите данные для поиска", font=("Arial Bold", 16))
    searchLabel.place(x=10, y=10)

window = Tk()
window.title("Телефонный Справочник")                       # Текст самого окна
window.geometry('1024x512')                                 # Размеры окна

mainLabel = Label(window, text = "Добро Пожаловать в редактор Телефонного Справочника\n\nВыберите во вкладке меню необходимую функцию", \
                                                                                                            font=("Arial Bold", 16))
mainLabel.place(x=100, y=20)
def MainLabelDel():
    mainLabel.place_forget()
    

def Add_interface_Del():
    destroy_object = [saveButton, clearTextButton, headerText, scrollTextBar, labelSurname, surname, labelName, name, labelSecondName, secondName, 
                     labelPhoneNumber, phoneNumber, labelCountry, country, labelCity, city, labelBirthDate, labelBirthDay, birthDay, labelBirthMonth, 
                     birthMonth, labelBirthYear, birthYear]
    for object_name in destroy_object:
        object_name.place_forget()

menu = Menu(window)
menuFind_item = Menu(menu, tearoff=0)  
menuFind_item.add_command(label='Добавление в справочник', command=lambda: [MainLabelDel(), Add_Interface()])        # (..., command = def)
menuFind_item.add_command(label='Поиск', command=lambda: [MainLabelDel(), Add_interface_Del(), Search_Interface()])
menu.add_cascade(label='Меню', menu=menuFind_item)
window.config(menu=menu)



window.mainloop()