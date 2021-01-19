from classes.vegetable import *

class Gardener:
    
    def plant_vegetable(self, type, number=0):

        type = str(type).lower()

        if (type == "carrot"):
            vegetable = Carrot()
            vegetable.grow(number)
            vegetable.type="Carrot"
            return vegetable
        
        if (type == "tomato"):
            vegetable = Tomato()
            vegetable.grow(number)
            vegetable.type="Tomato"
            return vegetable

        if (type == "pickle"):
            vegetable = Pickle()
            vegetable.grow(number)
            vegetable.type="Pickle"
            return vegetable

        else :
            raise Exception("Oups ! Nous n'avons plus de légume de type " + type + " en magasin...")

    def add(self, cls_garden, obj):

        try:
            if (cls_garden.vegetables[obj.type] + obj.seed) < 30:
                cls_garden.vegetables[obj.type] += obj.seed
            else:
                print('Jardin surchargé, ça va exploser ici ! Trouve un autre potager ! Merci !')
            
        except:
            if (obj.seed < 30):
                cls_garden.vegetables[obj.type] = obj.seed
            else:
                print('Jardin surchargé, le jardinier ne peut planter plus de 30 graines dans ce jardin !')
