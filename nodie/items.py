import json

from .regeneration import Regeneration
from .resources import Usable

class Item(Usable):

    def __init__(self, id, name, weight, duration, keys=None):
        super().__init__(keys)
        self.id = id
        self.name = name.lower()
        self.weight = weight
        self.duration = duration
        

class Equipment(Item):

    def __init__(self, id, name, weight, duration, slotType, regen, keys=None):
        super().__init__(id, name, weight, duration, keys)
        self.slotType = slotType
        self.regen = Regeneration(**regen)

    def __str__(self):
        dic = dict(self)
        dic['regen'] = dict(self.regen)
        return str(dic)


class Food(Item):

    def __init__(self, id, name, weight, duration, keys=None):
        super().__init__(id, name, weight, duration, keys)
