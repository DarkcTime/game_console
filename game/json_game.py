
import json  
from art import text2art
from class_game import Characters, Arm, Enemy
import random
import os
import menu

def input_someone():
    option = input("Нажмите enter")

def clear_console(): 
    os.system('cls||clear')

def open_file():
    f = open('game.json', encoding='UTF8')
    game = json.load(f)
    f.close()
    return game

def add_arm_to_json(_choised_arm):
    #получаем все данные из файла, перед последующей загрузкой
    f = open('game.json', 'r', encoding='UTF8')
    json_data = json.load(f)
    f.close()
    
    if json_data['character']['money'] >= _choised_arm.cost:
        #добавляем новое оружие для персонажа
        json_data['character']['money'] = json_data['character']['money'] - int(_choised_arm.cost)
        json_data['character']['items'].append(_choised_arm.name)
        json_data['character']['hp'] = json_data['character']['hp'] + _choised_arm.hp
        json_data['character']['damage'] = json_data['character']['damage'] + _choised_arm.damage
        #забираем оружие у торговца 
        json_data['seller']['money'] = json_data['seller']['money'] + int(_choised_arm.cost) 
        del json_data['items'][_choised_arm.name]

        #сохраняем внесённые изменения в файл
        f = open('game.json', 'w', encoding='UTF8')
        json.dump(json_data, f, sort_keys=False, indent=4,ensure_ascii=False, separators=(',',': '))
        f.close()
    else: 
        print("Пошел отсюда бомжара")
        input_someone()
        
def win_to_json(enemy):
    #получаем все данные из файла, перед последующей загрузкой
    f = open('game.json', 'r', encoding='UTF8')
    json_data = json.load(f)
    f.close()
    
    json_data['character']['money'] = json_data['character']['money'] + int(enemy.money)
    #косяк (поправить)
    json_data['character']['items'].append(enemy.items)
    json_data['character']['hp'] = json_data['character']['hp'] + int(enemy.money)

    f = open('game.json', 'w', encoding='UTF8')
    json.dump(json_data, f, sort_keys=False, indent=4,ensure_ascii=False, separators=(',',': '))
    f.close()
      

def spaces():
    print(f"\n\n\n")

def get_charter():
    _dict_data = open_file()
    charactes = Characters(_dict_data.get('character').get('name'), 
                           _dict_data.get('character').get('hp'),
                           _dict_data.get('character').get('damage'),
                           _dict_data.get('character').get('money'),
                           _dict_data.get('character').get('items'))
    return charactes

def print_money(): 
    print(f"У вас сейчас в кошельке только {get_charter().money} монет \n")

def print_characters():
    charter = get_charter()
    _result = f" Ваше имя: {charter.name} \n Остаток хп: {charter.hp} \n Ваш урон: {charter.damage} \n Количество денег: {charter.money} \n Предметы: {charter.items}"    
    title=text2art("character")
    print(title)    
    print(_result)
    spaces()

def print_characters_battle(charter):
    _result = f" Ваше имя: {charter.name} \n Остаток хп: {charter.hp} \n Ваш урон: {charter.damage} \n Количество денег: {charter.money} \n Предметы: {charter.items}"    
    title=text2art("character")
    print(title)    
    print(_result)
    spaces()

def get_random_enemy(_dict_data):
    list_enemy = []
    for k in _dict_data['enemy'].keys(): 
        list_enemy.append(k)
    return random.choice(list_enemy)

def get_enemy(): 
    _dict_data = open_file()
    name_random_enemy = get_random_enemy(_dict_data)
    enemy = Enemy(name_random_enemy, 
                           _dict_data.get('enemy').get(name_random_enemy).get('hp'),
                           _dict_data.get('enemy').get(name_random_enemy).get('damage'),
                           _dict_data.get('enemy').get(name_random_enemy).get('money'),
                           _dict_data.get('enemy').get(name_random_enemy).get('items'))
    return enemy



def print_battle(enemy, charter):
    title=text2art("Battle")
    print(title)
    print_characters_battle(charter)
    title=text2art("enemy") 
    print(title)
    _result = f" Злое имя: {enemy.name} \n Остаток хп: {enemy.hp} \n Ваш урон: {enemy.damage} \n Количество денег: {enemy.money} \n Предметы: {enemy.items}"            
    print(_result)

def print_arms():    
    _dict_data = open_file().get('items')
    i = 1
    dict_arms = {}  
    for k,v in _dict_data.items():
        arm = Arm(k, v['hp'], v['damage'], v['cost'])
        dict_arms[i] = arm
        _result = f" Название: {dict_arms.get(i).name} \n Дополнительное здоровье: {dict_arms.get(i).hp} \n Дополнительный урон: {dict_arms.get(i).damage} \n  Стоимость: {dict_arms.get(i).cost} золотых \n"
        print(f"Для выбора введите {i}")
        print(_result)
        i += 1
    return dict_arms



