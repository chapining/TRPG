import os
import random as rnd
import math
import casino

def  show_location_home(user_money):
    #описыва локацию
    os.system("cls")
    print("Ты у себя дома")
    print("1 - в казино")
    print("2 - ничего")

    #спросить пользователя
    choice = ""
    while choice not in ("1", "2"):
        #TODO: доделай вопрос!
        choice = input("Куда дальше? \n 1 или 2 \n вариант ответа:")
    #проверить ответ пользователя
    if choice == "1":
        show_location_casino(user_money)
    elif choice == "2":
        show_location_home(user_money)
    return user_money


def show_location_casino(user_money):
    #описыва локацию
    os.system("cls")
    print("Ты в казино")
    print("1 - домой")
    print("2 - ждать")
    print("3 - играть")
    choice = ""
    while choice not in ("1", "2", "3"):
        #TODO: доделай вопрос!
        choice = input("Куда дальше? \n 1, 2 или 3 \n вариант ответа:")
    #проверить ответ пользователя
    if choice == "1":
        show_location_home(user_money)
    elif choice == "2":
        show_location_casino(user_money)
    elif choice == "3":
       show_gamble(user_money)
    return user_money
    

def show_gamble(user_money):
    user_money = casino.play_dice(user_money)
    print(f"У вас теперь  {user_money}")
    input("Нажмите ENTER, чтобы вернуться в казино")
    show_location_casino(user_money)
    return user_money

# игра началась здесь
user_name = "Вася"
user_money = 5000
user_lock = 100 #TODO: сделать систему везения
show_location_home(user_money)

