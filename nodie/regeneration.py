

class Regeneration():

    soulTicks = 15
    soulGain = 1

    def __init__(self, hpTicks=0, hpGain=0, mpTicks=0, mpGain=0):
        self.hpTicks = hpTicks
        self.hpGain = hpGain
        self.mpTicks = mpTicks
        self.mpGain = mpGain
        
    @property
    def hpSec(self):
        if self.hpGain is None: return 0
        return self.hpGain/self.hpTicks

    @property
    def mpSec(self):
        if self.mpGain is None: return 0
        return self.mpGain/self.mpTicks

    @staticmethod
    def totalMpSec(reglist):
        return sum([r.mpSec for r in reglist])

    @staticmethod
    def totalHpSec(reglist):
        return sum([r.hpSec for r in reglist])

    @property
    def soulSec(self):
        if self.soulGain is None: return 0
        return self.soulGain/self.soulTicks
        
    @classmethod
    def from_mpSec(cls, mpSec):
        return cls(mpTicks=1, mpGain=mpSec)
        
    def __iter__(self):
        return iter(vars(self).items())

    def __str__(self):
        return str(dict(self))