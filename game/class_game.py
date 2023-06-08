class Characters(object):
    def __init__(self, name, hp, damage, money, items):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.money = money
        self.items = items

class Arm(object): 
    def __init__(self, name, hp, damage, cost): 
        self.name = name
        self.hp = hp
        self.damage = damage
        self.cost = cost
