from classes.garden import *
from classes.vegetable import *
from classes.gardener import *

# g = Garden()
# g.add(Carrot())

# p = Pickle()
# p.grow(8)
# g.add(p) 

# p.grow(52)
# g.add(p)

# print (g.seed) # display 8


Thib = Gardener()
Eden = Garden()

stock1 = Thib.plant_vegetable("carrot", 8)
stock2 = Thib.plant_vegetable("Pickle", 32)
stock3 = Thib.plant_vegetable("Tomato")
# stock4 = Thib.plant_vegetable("Potato")

stock3.grow(6)

Eden.add(stock1)
Eden.add(stock2)
Eden.add(stock3)


print (Eden.seed) # display 8