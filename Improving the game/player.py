from items import *
from map import rooms

def calculate_mass():
    cumulative_mass = 0
    for item in inventory:
        cumulative_mass+=item['mass']
    return cumulative_mass

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]
mass_limit = 4
player_mass = calculate_mass()


