import configparser, time

from nodie.spells import Spell
from nodie.items import Item, Equipment, Food
from nodie.character import Character, Vocation
from nodie.regeneration import Regeneration
from nodie.macros import RuneMaker

foods = Food.fromjson('data/items/food.json')
equipments = Equipment.fromjson('data/items/equipment.json')
spells = Spell.fromjson('data/spells/spells.json')
vocations = Vocation.fromjson('data/vocations/vocations.json')
for v in vocations: v.set_spells(spells)

cfg = configparser.ConfigParser()
cfg.read('config.ini')

characterName = cfg['Character']['name']
vocation = cfg['Character']['vocation']

vocation = [v for v in vocations if v.name == vocation][0]
char = Character(characterName, vocation)

# Rune Maker
rm = cfg['Rune Maker']
ring = [r for r in equipments if r.name.lower() == rm['ring'].lower()][0]
boots = [b for b in equipments if b.name.lower() == rm['boots'].lower()][0]
food = [f for f in foods if f.name.lower() == rm['food'].lower()][0]
runeSpell = [r for r in spells if r.name.lower() == rm['rune_spell'].lower()][0]
wasteSpell = [w for w in spells if w.name.lower() == rm['waste_spell'].lower()][0]

ring.read_cfg_keys()
boots.read_cfg_keys()
food.read_cfg_keys()
runeSpell.read_cfg_keys()
wasteSpell.read_cfg_keys()

print(ring.keys)
print(boots.keys)
print(food.keys)
print(runeSpell.keys)
print(wasteSpell.keys)

runeMaker = RuneMaker(char.vocation, ring, boots, food, runeSpell, wasteSpell)
runeMaker.activate_macros()
time.sleep(5)