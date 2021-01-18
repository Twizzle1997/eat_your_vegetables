from abc import ABC, abstractmethod

class Vegetable(ABC) :

    def __init__(self, seed = 0):
        self.seed = seed

    @abstractmethod
    def grow(self, number):
        self.seed =+ number


class Tomato(Vegetable) :
    def grow(self, number):
        self.seed =+ number

class Pickle(Vegetable) :
    def grow(self, number):
        self.seed =+ number

class Carrot(Vegetable) :
    def grow(self, number):
        self.seed =+ number
