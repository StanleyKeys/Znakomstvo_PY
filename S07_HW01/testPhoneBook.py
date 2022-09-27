from collections import UserList
from queue import Empty
from tkinter import *
from tkinter import scrolledtext
from tkinter import Menu
from tkinter.ttk import Combobox
from tkinter import ttk 

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
        with open('phoneDirectory.txt', 'a') as file:
            file.write(f'{surname.get()} ' + f'{name.get()} ' + f'{secondName.get()} ' + f'{phoneNumber.get()} ' + f'{country.get()} ' + f'{city.get()} ' + f'{birthDay.get()}{birthMonth.get()}{birthYear.get()} \n')
        Refresh_Scrollbar()

def Clear_Text_File():
    with open('phoneDirectory.txt', 'w') as file:
        file.write(' ')
    Refresh_Scrollbar()

def Refresh_Scrollbar():
    scrollTextBar.delete(1.0, END)                                            
    scrollTextBar.insert(INSERT, open('phoneDirectory.txt').read())

def Search_Button():
    
    infoGet = [surname.get(), name.get(), secondName.get(), phoneNumber.get(), country.get(), city.get(), birthDay.get(), birthMonth.get(), birthYear.get()]
    with open('phoneDirectory.txt') as f:
        for id, val in enumerate(infoGet):
            print(val)
            if val != '':
                if val in f.read():
                    combo.configure(state="enabled")
                    combo['value'] = infoGet
            

saveButton = Button(tab1, text="Сохранить", command=Save_Button_in_txt)
saveButton.place(x=5, y=250)
clearTextButton = Button(tab1, text="Очистить список", command=Clear_Text_File)
clearTextButton.place(x=300, y=250)
searchButton = Button(tab2, text="Поиск", command=Search_Button)
searchButton.place(x=20, y=200)


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

combo = Combobox(tab2, width=40, state="disabled")  
combo['values'] = (0)  
combo.current(0)  # установите вариант по умолчанию  
combo.place(x=20,y=250)

# combo = Combobox(tab2, width=40, state="disabled")  
# combo['values'] = (0)  
# combo.current(0)  # установите вариант по умолчанию  
# combo.place(x=20,y=250)

resLabel = Label(tab2, text=" ", font=("Arial Bold", 13))
resLabel.place(x=700,y=50)

window.mainloop()