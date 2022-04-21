from typing import List

from object import Object
from parametres import Parametres


class Bag(object):
    def __init__(self, objects: List[Object], isIn: List[bool] = None):
        self.objects = objects

        if not isIn:
            self.isIn = [Parametres.random.randint(0,1) for _ in range(Parametres.NB_OBJ)]
        else:
            self.isIn = isIn
        
        self.fitness = self.calcul_fitness()

    def calcul_fitness(self) -> int:
        #Pour le calcul du fitness, plus la valeur est petite, plus c'est positif.
        weight = 0

        for i in range(Parametres.NB_OBJ):
            obj = self.objects[i]
            weight += obj.weight * self.isIn[i]
        return max(Parametres.MAX - weight, 10)

    def calcul_weight(self) -> int:
        weight = 0
        for index in range(len(self.isIn)):
            weight += self.objects[index].weight * self.isIn[index]
        return weight

        
    def calcul_value(self) -> int:
        value = 0
        for index in range(len(self.isIn)):
            value += self.objects[index].value * self.isIn[index]
        return value

    @staticmethod
    def create_child(mere, pere):
        # 1 to have at least one part from the mother % -2 to have at least one part of the father
        mere_size = Parametres.random.randint(1, Parametres.NB_OBJ - 2)
        new_isIn = mere.isIn[:mere_size] + pere.isIn[mere_size:]
        child = Bag(mere.objects, new_isIn)
        child.mutate()
        return child

    def mutate(self):
        pass
    
    def __str__(self) -> str:
        return '[{}] Bag - Items : {} - Weight : {} - Value : {}'.format(self.calcul_fitness(), sum(self.isIn), self.calcul_weight(), self.calcul_value())