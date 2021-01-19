from classes.vegetable import *

class Gardener:
    
    def plant_vegetable(self, type, number=0):

        type = str(type).lower()

        if (type == "carrot"):
            vegetable = Carrot()
            vegetable.grow(number)
            return vegetable
        
        if (type == "tomato"):
            vegetable = Tomato()
            vegetable.grow(number)
            return vegetable

        if (type == "pickle"):
            vegetable = Pickle()
            vegetable.grow(number)
            return vegetable

        else :
            raise Exception("Oups ! Nous n'avons plus de légume de type " + type + " en magasin...")


            