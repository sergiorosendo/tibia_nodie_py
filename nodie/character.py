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
        with open(file) as f: 
            dic = json.load(f) 
        lst = dic[cls.__name__.lower() + 's']

        D = dict()
        for obj in lst:
            obj = cls(**obj)
            D[obj.name] = obj
        
        return D

    def set_spells(self, spells):
        self.spells = dict()
        if spells is None: return
        
        for sp in spells.values():
            if self.name in sp.vocations:
                self.spells[sp.name] = sp