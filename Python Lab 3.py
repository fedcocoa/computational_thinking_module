import random

player1 = {"name" : 'Kirill', 'health':100, 'ammo':50, 'experience':10000,'mana':50,'alive':True,'inventory':['sword','shield','potion']}

player1['inventory'].append('sword of azeroth')

def print_player(player):
    for key in player:
        print("{} is {}".format(key,player[key]))

def compute_experience(damage):
    return random.randint(0,damage*2)

def take_damage(player,damage):
    player['health']-=damage
    if player['health'] <= 0:
        player['alive'] = False
    player['experience']+=compute_experience(damage)
    return player

while(player1['alive']):
    player1 = take_damage(player1,5)
    print_player(player1)