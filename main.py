from object import Object
from parametres import Parametres
from population import Population

# Generate potential objects for the bag 
objects = [Object() for _ in range(Parametres.NB_OBJ)]

population = Population(objects)