from typing import List
from typing_extensions import Self
from genome import Genome

from object import Object
from parametres import Parametres


class Bag(Genome):
    def __init__(self, objects: List[Object], isIn: List[bool] = None) -> None:
        super().__init__()
        self.objects = objects
        if not isIn:
            self.genome = [Parametres.random.randint(0,1) for _ in range(Parametres.NB_OBJ)]
        else:
            self.genome = isIn
        self.fitness = self.evaluate()

    def calculate_weight(self) -> int:
        weight = 0
        for index in range(len(self.genome)):
            weight += self.objects[index].weight * self.genome[index]
        return weight

        
    def calculate_value(self) -> int:
        value = 0
        for index in range(len(self.genome)):
            value += self.objects[index].value * self.genome[index]
        return value

    def create_child(self, father: Self) -> Self:
        # 1 to have at least one part from the mother & -2 to have at least one part of the father
        mere_size = Parametres.random.randint(1, Parametres.NB_OBJ - 2)
        new_genome = self.genome[:mere_size] + father.genome[mere_size:]
        child = Bag(self.objects, new_genome)
        child.mutate()
        return child

    def mutate(self):
        pass

    def evaluate(self) -> float:
        #Pour le calcul du fitness, plus la valeur est petite, plus c'est positif.
        weight = 0
        for i in range(Parametres.NB_OBJ):
            obj = self.objects[i]
            weight += obj.weight * self.genome[i]
        return max(Parametres.MAX - weight, 10)
    
    def __str__(self) -> str:
        return '[{}] Bag - Items : {} - Weight : {} - Value : {}'.format(self.evaluate(), sum(self.genome), self.calculate_weight(), self.calculate_value())