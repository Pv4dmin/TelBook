
from random import *
import json
import easygui as g
from easygui import *

phonebook = {
             "Иван": {"Номер телефона": "81112223344", "адрес": "ул. Пушкина д. Калатушкина"},
             "Федя": {"Номер телефона": "89998887766", "адрес": "ул. Ленина д. на Поленина"}
             }

def save():
    with open("phoneNumber.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(phonebook, ensure_ascii=False))
        
        print("Справочник был успешно сохранен в файле: phoneNumber.json")

def load():
    with open("phoneNumber.json", "r", encoding="utf-8") as fh:
        phonebook = json.load(fh)
    print("Справочник был успешно загружен")  

try:
    with open("phoneNumber.json", "r", encoding="utf-8") as fh:
        phonebook = json.load(fh)
    print("Справочник был успешно загружен")  
except:
    phonebook = {
                "Иван": {"Номер телефона": "81112223344", "адрес": "ул. Пушкина д. Калатушкина"},
                "Федя": {"Номер телефона": "89998887766", "адрес": "ул. Ленина д. на Поленина"}
                }

while True:
    command = input("Введите команду: ")
    if command == "/stop":
        save()
        print("Бот остановил свою работу. Заходите ещё")
        break

    elif command == "/add":
        name = input("Введите имя контакта: ")
        if name in phonebook:
            print("Такой абонент уже присутствует в справочнике")
        else:
            number = input("Введите номер телефона: ")
            address = input("Введите адрес: ")
            phonebook[name] = {"Номер телефона": number, "адрес": address}
            print(f"Абонент '{name}' был успешно добавлен в справочник")
    
    elif command == "/edit":
        name_edit = input("Введите имя контакта: ")
        if name_edit in phonebook:
            number = input("Введите новый номер телефона: ")
            address = input("Введите новый адрес: ")
            phonebook[name_edit] = {"номер": number, "адрес": address}
            print("Контакт успешно изменен")
        else:
            print("Контакт не найден")
    elif command == "/search":
        name_search = input("Введите имя контакта для поиска: ")
        if name_search in phonebook:
            print(phonebook[name_search])    
    elif command == "/show":
        for key, values in phonebook.items():
                print("{0}: {1}, {2}".format(key, values["Номер телефона"], values["адрес"]))
    elif command == "/save":
        save()
    elif command == "/delete":
        name_del = input("Введите имя контакта: ")
        if name_del in phonebook:
            del phonebook[name_del]
            print("Контакт успешно удален")
        else:
            print("Контакт не найден")
    elif command == "/load":
        load()
    else:
        print("Неопознанная команда. Просьба изучить мануал через команду /help")
