from abc import ABC, abstractmethod

class Vegetable(ABC) :

    def __init__(self, seed = 0, type="none"):
        self.seed = seed
        self.type = type

    @abstractmethod
    def grow(self, number):
        pass


class Tomato(Vegetable) :
    def grow(self, number):
        self.seed =+ number

class Pickle(Vegetable) :
    def grow(self, number):
        self.seed =+ number

class Carrot(Vegetable) :
    def grow(self, number):
        self.seed =+ number

