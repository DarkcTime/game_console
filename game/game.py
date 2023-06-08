from art import text2art
from menu import print_first_menu,print_shop_menu, print_buy_menu
from json_game import print_characters, print_arms
import os

def clear_console(): 
    os.system('cls||clear')

def input_choice_some():
    option = int(input('Выберите пункт меню: '))
    return option

def print_title_game(_title):
    _art = text2art(_title, font="block", chr_ignore=True)
    print(_art)

def shop_menu():
    clear_console() 
    menu_title = text2art("shop")
    print(menu_title)
    data_arms = print_arms()
    print_shop_menu(data_arms) 
    choiced = input_choice_some()
    if choiced == 0: 
        first_menu()
    else:
        clear_console()
        choised_arm = data_arms.get(choiced)
        print(f"{choised_arm.name} стоит {choised_arm.cost} монет. \n")
        print_buy_menu()
        choiced = input_choice_some()

        


def first_menu():
    print_first_menu()
    choiced = input_choice_some()
    match choiced:
        case 1:
            #вывести характеристики
            print_characters()
            first_menu()
        case 2: 
            #купить предмет
            shop_menu()        
        case 3:
            #идти сражаться 
            exit()
        case  4:
            #выход 
            exit()          

TITLE = "gpy"; 
MANUAL = f"instruction for play this game"


#вывод названия нашей игры
print_title_game(TITLE)
#вывод инструкцию по 
print(MANUAL)

clear_console()
first_menu()