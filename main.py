from classes.garden import *
from classes.vegetable import *

g = Garden()
g.add(Carrot())

p = Pickle()
p.grow(8)
g.add(p) 

p.grow(52)
g.add(p)

print (g.seed) # display 8