
import json  
from art import text2art
from class_game import Characters, Arm

def open_file():
    f = open('game.json', encoding='UTF8')
    game = json.load(f)
    return game

def spaces():
    print(f"\n\n\n")


def print_characters():
    _dict_data = open_file()
    charactes = Characters(_dict_data.get('character').get('name'), 
                           _dict_data.get('character').get('hp'),
                           _dict_data.get('character').get('damage'),
                           _dict_data.get('character').get('money'),
                           _dict_data.get('character').get('items'))
    _result = f" Ваше имя: {charactes.name} \n Остаток хп: {charactes.hp} \n Ваш урон: {charactes.damage} \n Количество денег: {charactes.money} \n Предметы: {charactes.items}"    
    title=text2art("Parameters")
    print(title)    
    print(_result)
    spaces()

def print_arms():    
    _dict_data = open_file().get('items')
    i = 1
    dict_arms = {}  
    for k,v in _dict_data.items():
        arm = Arm(k, v['hp'], v['damage'], v['cost'])
        dict_arms[i] = arm
        _result = f" Название: {dict_arms.get(i).name} \n Дополнительное здоровье: {dict_arms.get(i).hp} \n Дополнительный урон: {dict_arms.get(i).damage} \n"
        print(f"Для выбора введите {i}")
        print(_result)
        i += 1
    return dict_arms



