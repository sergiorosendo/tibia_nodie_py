import configparser, time

from nodie.usables.spells import Spell
from nodie.usables.items import Item, Equipment, Food
from nodie.character import Character, Vocation
from nodie.regeneration import Regeneration
from nodie.macros.rune_maker import RuneMaker

foods = Food.fromjson('data/items/food.json')
equipments = Equipment.fromjson('data/items/equipment.json')
spells = Spell.fromjson('data/spells/spells.json')
vocations = Vocation.fromjson('data/vocations/vocations.json')

for key, value in vocations.items():
    value.set_spells(spells)

cfg = configparser.ConfigParser()
cfg.read('config.ini')

characterName = cfg['Character']['name']
vocation = vocations[cfg['Character']['vocation']]
char = Character(characterName, vocation)

# Rune Maker
rm = cfg['Rune Maker']
ring = equipments[rm['ring'].lower()]
boots = equipments[rm['boots'].lower()]
food = foods[rm['food'].lower()]
runeSpell = spells[rm['rune_spell'].lower()]
wasteSpell = spells[rm['waste_spell'].lower()]

ring.read_cfg_keys()
boots.read_cfg_keys()
food.read_cfg_keys()
runeSpell.read_cfg_keys()
wasteSpell.read_cfg_keys()

runeMaker = RuneMaker(char.vocation, ring, boots, food, runeSpell, wasteSpell)
runeMaker.activate_macros()
time.sleep(5)