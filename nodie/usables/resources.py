import random, configparser, json, os

from ..win_api import send_key


class Usable():

    def __init__(self, keys=None):
        self._keys = keys

    @property
    def keys(self):
        return self._keys
    
    @keys.setter
    def keys(self, keys):
        self._keys = keys

    def use(self):
        send_key(random.choice(self.keys))

    def read_cfg_keys(self):
        cfgKeys = configparser.ConfigParser()
        cfgKeys.read('hotkeys.ini')

        usables = cfgKeys['Usables']
        self.keys = usables.get(self.name.lower().replace(' ', '_'), None)
        self.keys = self.keys.replace(' ', '').split(',')

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

    def img(self):
        pass

    def __iter__(self):
        return iter(vars(self).items())

    def __str__(self):
        return str(self.__dict__)



