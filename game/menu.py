from art import text2art


def print_menu(_menu_options):
    for key in _menu_options.keys():
        print (key, '--', _menu_options[key] )

def print_first_menu(): 
    menu_title = text2art("menu")
    print(menu_title)
    print_menu(first_menu_options)

def print_shop_menu(list_arms):
    shop_menu_options[f"1-{len(list_arms.items())}"] = "Выберите предмет для покупки"
    shop_menu_options[0] = "Вернуться в главное меню" 
    print_menu(shop_menu_options)

def print_buy_menu():
    print_menu(buy_menu_options)

def print_battle_menu():
    print(battle_menu_options[0])

def print_battle_win():
    print(win_menu_options[0])

def print_battle_wasted():
    print(wasted_menu_options[0])

first_menu_options = {
    1: 'Посмотреть характеристики',
    2: 'Купить предмет',
    3: 'Идти сражаться',
    4: 'Покинуть нас(',
}

shop_menu_options = {}

buy_menu_options = {
    1: 'Купить', 
    2: 'Свалить из магазина'
}

battle_menu_options = [
    'Сразиться'
]

win_menu_options = [
    'Вернуться в главное меню'
]


wasted_menu_options = [
    'Закончить игру'
]
