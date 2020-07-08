from abc import ABC, abstractmethod
from threading import Thread
from time import sleep
import random

from ..win_api import send_key


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