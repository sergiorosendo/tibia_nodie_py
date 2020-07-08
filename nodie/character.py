import json

from .regeneration import Regeneration


class Character():

    def __init__(self, name, vocation, runeMaker=None):
        self.lv = 8
        self.name = name
        self.vocation = vocation
        self.runeMaker = runeMaker

    @property
    def maxHp(self):
        return 185 + (self.lv - 8)*self.vocation.hpLvlUp
    
    @property
    def maxMp(self):
        return 90 + (self.lv - 8)*self.vocation.mpLvlUp 


class Vocation():

    def __init__(self, id, name, capLvUp, hpLvUp, mpLvUp, regen, spells=None):
        self.id = id
        self.name = name
        self.capLvUp = capLvUp
        self.hpLvUp = hpLvUp
        self.mpLvUp = mpLvUp
        self.regen = Regeneration(**regen)
        self.set_spells(spells)

    def __iter__(self):
        return iter(vars(self).items())

    def __str__(self):
        dic = dict(self)
        dic['regen'] = dict(self.regen)
        return str(dic)

    @classmethod
    def fromjson(cls, file):
        V = []
        with open(file) as f:
            dic = json.load(f)
        
        if 'vocations' in dic:
            lst = []
            for obj in dic['vocations']:
                lst.append(cls(**obj))
            return lst
        return cls(**dic)

    def set_spells(self, spells):
        self.spells = []
        if spells is None: return
        for sp in spells:
            if self.name in sp.vocations:
                self.spells.append(sp)