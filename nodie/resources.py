import random, configparser, json, os

from .win_api import send_key

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
        #print(os.path.join('hotkeys.ini'))
        cfgKeys.read('hotkeys.ini')

        usables = cfgKeys['Usables']
        self.keys = usables.get(self.name.lower().replace(' ', '_'), None)
        self.keys = self.keys.replace(' ', '').split(',')

    @classmethod
    def fromjson(cls, file):
        with open(file) as f: 
            dic = json.load(f) 
    
        lst = []
        for obj in dic[cls.__name__.lower() + 's']:
            lst.append(cls(**obj))
        return lst

    def img(self):
        pass

    def __iter__(self):
        return iter(vars(self).items())

    def __str__(self):
        return str(dict(self))



