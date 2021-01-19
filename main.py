from classes.garden import *
from classes.vegetable import *
from classes.gardener import *

Thib = Gardener()
Eden = Garden()

stock1 = Thib.plant_vegetable("carrot", 8)
stock2 = Thib.plant_vegetable("Pickle", 32)
stock3 = Thib.plant_vegetable("Tomato")
stock4 = Thib.plant_vegetable("Carrot", 3)

stock3.grow(6)

Thib.add(Eden, stock1)
Thib.add(Eden, stock2)
Thib.add(Eden, stock3)
Thib.add(Eden, stock4)

print (Eden.vegetables)

nb_seed = Eden.count_type()
print (nb_seed)