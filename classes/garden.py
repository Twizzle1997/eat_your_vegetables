from abc import ABC

class Garden :

    def __init__(self, seed=0):
        self.seed = seed

    def _plant(self, cls): 
        return cls

    def add(self, cls):
        self._plant(cls)
        self.seed = self.seed + cls.seed
