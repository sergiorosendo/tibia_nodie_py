
    def __add__(self, other):
        self.hpTicks += other.hpTicks
        self.hpGain += other.hpGain
        self.mpTicks += other.mpTicks
        self.mpGain += other.mpGain

    def __sub__(self, other):
        self.hpTicks -= other.hpTicks
        self.hpGain -= other.hpGain
        self.mpTicks -= other.mpTicks
        self.mpGain -= other.mpGain



        if isinstance(action, Spell):
            self.tdelta = (-0.05*action.cd, 0.05*action.cd)
        elif isinstance(action, Food):
            self.tdelta = (0, 100)
        elif isinstance(action, Equipment):
            if action.duration >= 10000:
                self.tdelta = ()
            self.tdelta = (1000, 1000 + 0.015*action.duration) 


    def execute(self):
        self.


        self.equipment = {
            'head': None, 
            'legs': None, 
            'amulet': None, 
            'backpack': None, 
            'ammo': None, 
            'weapon': None, 
            'shield': None, 
            'armor': None, 
            'ring': None
            }


from abc import ABC, abstractmethod

class Macro(ABC):

    def __init__(self):
        pass

    def act(self):
        key = random.choice(self.keys)
        sleepPeriod = self.cd + self.delta
        # send key self.randomKey, sleep self.sleepPeriod, act loop

    @property
    def sleepPeriod(self):
        return self.cd + self.delta

    @property
    def randomKey(self):
        return random.choice(self.keys)

    @property
    @abstractmethod
    def cd(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def delta(self):
        raise NotImplementedError

class RuneMacro(Macro):

    def __init__(self, spell, keys, regen):
        self.spell = spell
        self.keys = list(keys)
        self.regen = regen
 
    @property
    def cd(self):
        return max(self.soulPeriod, self.manaPeriod)

    @property
    def soulPeriod(self):
        return self.spell.soul/self.regen.soulSec

    @property
    def manaPeriod(self):
        return self.spell.mana/self.regen.mpSec

    @property
    def extraMpSec(self):
        # ToDo: if extraMpSec > 0 create manawasting macro
        if self.soulPeriod < self.manaPeriod: return 0
        return (self.soulPeriod - self.manaPeriod)*self.regen.mpSec

    @property
    def delta(self):
        # lower minimum delta allows the character to make use of high starting soul points
        return random.randrange(-self.cd*0.07, self.cd*0.04)

class WasteMacro(Macro):

    def __init__(self, spell, keys, regen):
        self.spell = spell
        self.keys = list(keys)
        self.regen = regen
 
    @property
    def cd(self):
        return self.manaPeriod

    @property
    def manaPeriod(self):
        return self.spell.mana/self.regen.mpSec

    @property
    def delta(self):
        # lower minimum delta allows the character to make use of high starting soul points
        return random.randrange(-self.cd*0.05, self.cd*0.05)

class EquipmentMacro(Macro):    

    def __init__(self, item, keys):
        self.item = item
        self.keys = list(keys)

    @property
    def cd(self):
        return min(self.item.duration, 300000)

    @property
    def delta(self):
        return random.randrange(2000, 6000)

class FoodMacro(Macro):
    
    def __init__(self, item):
        self.item = item

    @property
    def cd(self):
        return self.item.duration

    @property
    def delta(self):
        return random.randrange(-self.cd*0.2, -self.cd*0.1)


   def set_macros(self):
        self.macros = []
        if self.runeSpell is not None:
            self.runeMacro = RuneMacro(self.runeSpell, runeSpellKeys, self.regen)
            if (self.wasteSpell is not None) and (self.RuneMacro.extraMpSec > 0):
                self.wasteMacro = WasteMacro(self.wasteSpell, wasteSpellKeys, Regeneration.from_mpSec(self.RuneMacro.extraMpSec))
        if self.ring is not None:
            self.ringMacro = EquipmentMacro(self.ring, ringKeys)
        if self.boots is not None:        
            self.bootsMacro = EquipmentMacro(self.boots, bootsKeys)
        if self.amulet is not None:
            self.amuletMacro = EquipmentMacro(self.amulet, amuletKeys)
        if self.food is not None:
            self.foodMacro = FoodMacro(self.food, foodKeys)

    def activate_macros(self):
        
        if self.runeMacro is not None: 
            self.runeMacro.run()
        if self.wasteMacro is not None:
            self.wasteMacro.run()
        self.wasteMacro.run()
        pass

    
    with open('../data/vocations/vocations.xml') as inFh:
    with open('../data/vocations/vocations.json', 'w') as outFh:
        json.dump(xmltodict.parse(inFh.read()), outFh , sort_keys=True, indent=4)


from collections import defaultdict

def dicvalues(dic, keys):
    ddic = defaultdict(None, dic)
    return (ddic.get(key) for key in keys)



class RuneMaker():

    def __init__(self, vocation, ring=None, boots=None, food=None, runeSpell=None, wasteSpell=None, hotkey=None):
        self.vocation = vocation
        self.ring = ring
        self.boots = boots
        self.runeSpell = runeSpell
        self.wasteSpell = wasteSpell
        self.food = food
        self.hotkey = hotkey
        self.set_macros()

    @property
    def regen(self):
        mpSec = 0
        if self.vocation is not None: mpSec += self.vocation.regen.mpSec
        if self.ring is not None: mpSec += self.ring.regen.mpSec
        if self.boots is not None: mpSec += self.boots.regen.mpSec
        mpSec *= 2  # Double Regen in protection zone
        regen = Regeneration.from_mpSec(mpSec)
        return regen

    def set_macros(self):
        if self.ring: self.ringMacro = EquipmentMacro(self.ring, ringKeys)
        if self.boots: self.bootsMacro = EquipmentMacro(self.boots, bootsKeys)
        if self.food: self.foodMacro = FoodMacro(self.food, foodKeys)    
        if self.runeSpell: self.runeMacro = RuneMacro(self.runeSpell, runeSpellKeys, self.regen)
        if (self.runeSpell) and (self.RuneMacro.extraMpSec > 0) and (self.wasteSpell is not None):
            self.wasteMacro = WasteMacro(self.wasteSpell, wasteSpellKeys, Regeneration.from_mpSec(self.RuneMacro.extraMpSec))

    def _reset_macros(self):
        # TODO: check if threads need to be killed manually
        # probably yes
        self.runeMacro = None
        self.wasteMacro = None
        self.ringMacro = None
        self.bootsMacro = None
        self.helmetMacro = None
        self.foodMacro = None

    def activate_macros(self):
        if self.ringMacro: self.ringMacro.start()
        if self.bootsMacro: self.bootsMacro.start()
        if self.foodMacro: self.foodMacro.start()        
        if self.runeMacro: self.runeMacro.start()
        if self.wasteMacro: self.wasteMacro.start()

    def deactivate(self):
        # suspend or kill each macro's thread
        pass

[Knight]
exura_ico =
exura_gran_ico =
ultimate_health_potion =
supreme_health_potion =
haste = 

[Sorcerer]
light_healing =
great_healing =
ultimate_healing = 
mana_potion =
haste = 

[Paladin]
exura_gran_san =
great_spirit_potion =
ultimate_spirit_potion =
haste = 
[Food]
brown_mushroom = e, f

[Equipment]



ring_keys = cfg['Rune Maker']['ring_keys'].replace(' ', '').split(',')
boots_keys = cfg['Rune Maker']['boots_keys'].replace(' ', '').split(',')
food_keys = cfg['Rune Maker']['food_keys'].replace(' ', '').split(',')
rune_spell_keys = cfg['Rune Maker']['rune_spell_keys'].replace(' ', '').split(',')
waste_spell_keys = cfg['Rune Maker']['waste_spell_keys'].replace(' ', '').split(',')