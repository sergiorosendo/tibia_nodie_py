from abc import ABC, abstractmethod
from threading import Thread
from time import sleep
import random

from .win_api import send_key
from .items import Item, Equipment, Food
from .regeneration import Regeneration

class Macro(Thread, ABC):

    def __init__(self):
        Thread.__init__(self, daemon=True)
        ABC.__init__(self)

    def act(self):
        key = random.choice(self.keys)
        sleepPeriod = self.cd + self.delta
        # send key self.randomKey, sleep self.sleepPeriod, act loop

    @property
    def sleepPeriod(self):
        return self.cd + self.delta

    @property
    @abstractmethod
    def cd(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def delta(self):
        raise NotImplementedError

    def run(self):
        sleep(random.uniform(1, 5))
        
        while True:
            self.usable.use()
            sleep(self.cd + self.delta)


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