import random
from time import sleep

from .macros import Macro
from ..regeneration import Regeneration


class SpellMacro(Macro):

    def __init__(self, spell, regen):
        super().__init__()
        self.spell = spell
        self.regen = regen
        
    @property
    def usable(self):
        return self.spell

    @property
    def manaPeriod(self):
        return self.spell.mana/self.regen.mpSec

    @property
    def soulPeriod(self):
        return self.spell.soul/self.regen.soulSec

    @property
    def cd(self):
        return max(self.soulPeriod, self.manaPeriod)


class RuneSpellMacro(SpellMacro):

    def __init__(self, spell, regen):
        super().__init__(spell, regen)

    @property
    def extraMpSec(self):
        if self.soulPeriod < self.manaPeriod: return 0
        return (self.soulPeriod - self.manaPeriod)*self.regen.mpSec/self.cd

    @property
    def delta(self):
        # lower minimum delta allows the character to make use of high starting soul points
        return random.uniform(-self.cd*0.07, self.cd*0.04)


class WasteSpellMacro(SpellMacro):

    def __init__(self, spell, regen):
        super().__init__(spell, regen)
 
    @property
    def delta(self):
        return random.uniform(-self.cd*0.05, self.cd*0.05)


class ItemMacro(Macro):

    def __init__(self, item):
        super().__init__()
        self.item = item
    
    @property
    def usable(self):
        return self.item


class EquipmentMacro(ItemMacro):    

    def __init__(self, item):
        super().__init__(item)

    @property
    def cd(self):
        return min(self.item.duration, 300)

    @property
    def delta(self):
        return random.uniform(2, 6)


class FoodMacro(ItemMacro):
    
    def __init__(self, item):
        super().__init__(item)

    @property
    def cd(self):
        return self.item.duration

    @property
    def delta(self):
        return random.uniform(-self.cd*0.2, -self.cd*0.1)


class RuneMaker():

    def __init__(self, vocation, ring, boots, food, runeSpell, wasteSpell, hotkey=None):
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
        self._reset_macros()
        if self.ring: self.ringMacro = EquipmentMacro(self.ring)
        if self.boots: self.bootsMacro = EquipmentMacro(self.boots)
        if self.food: self.foodMacro = FoodMacro(self.food)    
        if self.runeSpell: self.runeSpellMacro = RuneSpellMacro(self.runeSpell, self.regen)
        if self.runeSpell and self.wasteSpell and self.runeSpellMacro.extraMpSec > 0:
            self.wasteSpellMacro = WasteSpellMacro(self.wasteSpell, Regeneration.from_mpSec(self.runeSpellMacro.extraMpSec))

    def _reset_macros(self):
        # TODO: check if threads need to be killed manually. Probably yes
        self.ringMacro, self.bootsMacro, self.foodMacro, self.runeSpellMacro, self.wasteSpellMacro = None, None, None, None, None

    def activate_macros(self):
        for macro in self.macros:
            macro.start()
            sleep(random.uniform(0, 0.25))

    @property
    def macros(self):
        return [self.ringMacro, self.bootsMacro, self.foodMacro, self.runeSpellMacro, self.wasteSpellMacro]

    def deactivate(self):
        # suspend or kill each macro's thread
        pass