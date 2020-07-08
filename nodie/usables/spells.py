import json

from .resources import Usable

class Spell(Usable):

    def __init__(self, vocations, group, id, name, words, mana, soul, cd, groupCd, keys=None):
        super().__init__(keys)
        self.vocations = vocations
        self.group = group
        self.id = id
        self.name = name.lower()
        self.words = words
        self.mana = mana
        self.soul = soul
        self.cd = cd
        self.groupCd = groupCd

