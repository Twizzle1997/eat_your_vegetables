from abc import ABC

class Garden :

    def __init__(self, total_seed=0):
        self.seed = total_seed
        self.vegetables = {}

    def _plant(self, cls): 
        return cls

    # def add(self, cls):
    #     self._plant(cls)
        
    #     if (self.seed + cls.seed) > 30:
    #         print('Jardin surchargé, ça va exploser ici ! Trouve un autre potager ! Merci !')
        
    #     else:
    #         self.seed += cls.seed

    def count_type(self):
        return len(self.vegetables)