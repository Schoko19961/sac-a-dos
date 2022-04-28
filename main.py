from bag import Bag
from object import Object
from parametres import Parametres
from population import Population

# Generate potential objects for the bag 
objects = [Object() for _ in range(Parametres.NB_OBJ)]
bags = [Bag(objects) for _ in range(Parametres.POPULATION_SIZE)]
population = Population(bags)
population.run()