from art import text2art
from menu import print_first_menu,print_shop_menu, print_buy_menu, print_battle_menu, print_battle_win, print_battle_wasted
from json_game import print_characters, print_arms, add_arm_to_json, print_battle, print_money, clear_console, get_enemy, get_charter, win_to_json, input_someone
import os
import random

def input_choice_some():
    option = int(input('Выберите пункт меню: '))
    return option


def get_rand_res():
    return random.randint(1,6)

def print_title_game(_title):
    _art = text2art(_title, font="block", chr_ignore=True)
    print(_art)

def shop_menu():
    clear_console() 
    menu_title = text2art("shop")
    print(menu_title)
    print_money()
    data_arms = print_arms()
    print_shop_menu(data_arms) 
    choiced = input_choice_some()
    if choiced == 0:
        clear_console() 
        first_menu()
    else:
        clear_console()
        choised_arm = data_arms.get(choiced)
        print(f"{choised_arm.name} стоит {choised_arm.cost} монет. \n")
        print_buy_menu()
        choiced = input_choice_some()
        if choiced == 0: 
            first_menu()
        else:
            add_arm_to_json(choised_arm)
            first_menu()


def battle():
    clear_console()
    enemy = get_enemy()
    charter = get_charter()
    while True:
        rand_res = get_rand_res()                
        print_battle(enemy, charter)
        print_battle_menu()
        input_someone()
        if rand_res > 3:
            clear_console()
            print(f"нанесено {charter.damage} урона")     
            enemy.hp = enemy.hp - charter.damage
        else:
            clear_console()
            print(f"получено {enemy.damage} урона")
            charter.hp = charter.hp - enemy.damage                
                    
        if enemy.hp <= 0:
            title=text2art("win")
            print(title)
            print_battle_win()
            win_to_json(get_enemy())
            input_someone()
            clear_console()
            first_menu()
            break
        if charter.hp <= 0:
            title=text2art("wasted")
            print(title)
            print_battle_wasted()
            input_someone()
            exit()


def first_menu():
    print_first_menu()
    choiced = input_choice_some()
    match choiced:
        case 1:
            #вывести характеристики
            clear_console()
            print_characters()
            input_someone()
            clear_console()
            #вывод названия нашей игры
            print_title_game(TITLE)
            #вывод инструкцию по 
            print(MANUAL)
            first_menu()
        case 2: 
            #купить предмет
            shop_menu()        
        case 3:
            #идти сражаться
            battle()            
        case  4:
            #выход 
            exit()          
    

TITLE = "RPG_HERO"; 
MANUAL = f"Добро пожаловать в игру, мы старались \n Наслаждайтесь)))"

clear_console()
#вывод названия нашей игры
print_title_game(TITLE)
#вывод инструкцию по 
print(MANUAL)

first_menu()