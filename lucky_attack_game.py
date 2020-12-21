import random

class Hero:
    def __init__(self, name, healthPoint, attackPoint, defencePoint, manaPoint):
        self.name = name
        self.healthPoint = healthPoint
        self.attackPoint = attackPoint
        self.defencePoint = defencePoint
        self.manaPoint = manaPoint

    # Method for attack
    def attack(self, enemy): 
        print(self.name + ' attacks ' + enemy.name)
        enemy.defend(self, self.attackPoint)
    
    # Method for speacial attack
    def spAttack(self, enemy):
        if (self.manaPoint != 0):
            print(self.name + ' is using special attack to ' + enemy.name)
            enemy.defend(self, self.attackPoint + self.manaPoint * 1)
            self.manaPoint -= 1 # everytime uses sp attack, mana point min 1
            print(self.name + ' MP: ' + str(self.manaPoint))
        else:
            print(self.name + ' has no MP') # if player doesn't have MP, can't use special attack
    
    def defend(self, enemy, attackPoint_enemy):
        attack_received = attackPoint_enemy - self.defencePoint * 0.5
        print('Hit: ' + str(attack_received))
        self.healthPoint -= attack_received
        print(self.name + ' HP: ' + str(self.healthPoint))

# Type of heroes (inherit from class Hero)
class Knight(Hero):
    def __init__(self, name):
        self.name = name
        self.healthPoint = 100
        self.attackPoint = 7
        self.defencePoint = 7
        self.manaPoint = 7

class Assassin(Hero):
    def __init__(self, name):
        self.name = name
        self.healthPoint = 100
        self.attackPoint = 9
        self.defencePoint = 5
        self.manaPoint = 7

class Mage(Hero):
    def __init__(self, name):
        self.name = name
        self.healthPoint = 100
        self.attackPoint = 5
        self.defencePoint = 5
        self.manaPoint = 11

# Method for the fight
def play_game(p1, p2):
        # print(p1.healthPoint)
    while(p1.healthPoint != 0 and p2.healthPoint != 0):
        step = random.randint(0, 3)
        if(step == 0):
            p1.attack(p2)
            print('\n')
        elif(step == 1):
            p2.attack(p1)
            print('\n')
        elif(step == 2):
            p1.spAttack(p2)
            print('\n')
        elif(step == 3):
            p2.spAttack(p1)
            print('\n')
        
        if(p1.healthPoint <= 0):
            print(p1.name + ' is KO')
            print('The winner is ' + p2.name)
            break
        elif(p2.healthPoint <= 0):
            print(p2.name + ' is KO')
            print('The winner is ' + p1.name)
            break
    return

# Main Program
print('''
      Player 1
      1. Knight
      2. Assassin
      3. Mage
      ''')
type = input('Choose your type: ')
name = input('Type your name: ')
if(type == 1):
    player1 = Knight(name)
elif(type == 2):
    player1 = Assassin(name)
elif(type == 3):
    player1 = Mage(name)
else:
    player1 = Knight(name)

print('''
      Player 2
      1. Knight
      2. Assassin
      3. Mage
      ''')
type = input('Choose your type: ')
name = input('Type your name: ')
if(type == 1):
    player2 = Knight(name)
elif(type == 2):
    player2 = Assassin(name)
elif(type == 3):
    player2 = Mage(name)
else:
    player2 = Knight(name)

# =========Game Start!!!!==========
play_game(player1, player2)
