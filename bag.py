from typing import List
from typing_extensions import Self
from genome import Genome

from object import Object
from parametres import Parametres


class Bag(Genome):
    def __init__(self, objects: List[Object], genome: List[bool] = None) -> None:
        super().__init__()
        self.objects = objects
        if not genome:
            self.genome = [Parametres.random.randint(0,1) for _ in range(Parametres.NB_OBJ)]
        else:
            self.genome = genome

    def calculate_weight(self) -> int:
        weight = 0
        for obj, isIn in zip(self.objects, self.genome):
            weight += obj.weight * isIn
        return weight

        
    def calculate_value(self) -> int:
        value = 0
        for obj, isIn in zip(self.objects, self.genome):
            value += obj.value * isIn
        return value

    def create_child(self, father: Self) -> Self:
        # 1 to have at least one part from the mother & -2 to have at least one part of the father
        mere_size = Parametres.random.randint(1, Parametres.NB_OBJ - 2)
        new_genome = self.genome[:mere_size] + father.genome[mere_size:]
        child = Bag(self.objects, new_genome)
        child.mutate()
        return child

    def mutate(self):
        mutate_factor = Parametres.random.random()
        if mutate_factor > Parametres.MUTATION_PROP:
            pass
        mutation_count = Parametres.random.randint(1, Parametres.MAX_MUTATION_COUNT)
        for _ in range(mutation_count):
            rnd = Parametres.random.random()
            if rnd < 0.5:
                # Mutation variation 1: Echange un objet pour un autre
                pos1 = Parametres.random.randint(0, len(self.genome) - 1)
                pos2 = Parametres.random.randint(0, len(self.genome) - 1)
                tmp = self.genome[pos1]
                self.genome[pos1] = self.genome[pos2]
                self.genome[pos2] = tmp
            else:
                # Mutation variation 2: Sors / Ajoute un objet au sac a dos
                pos = Parametres.random.randint(0, len(self.genome) - 1)
                self.genome[pos] = not self.genome[pos]

    def evaluate(self) -> float:
        # Pour le calcul du fitness, plus la valeur est grande, plus c'est positif.
        value = self.calculate_value()
        weight = self.calculate_weight()
        if(weight > Parametres.BAG_WEIGHT_MAX):
            self.fitness = 0
        else:
            self.fitness = value - weight / 10
        return self.fitness
    
    def __str__(self) -> str:
        return '[{}] Bag - Items : {} - Weight : {}/{} - Value : {}'.format(self.evaluate(), sum(self.genome), self.calculate_weight(), Parametres.BAG_WEIGHT_MAX ,self.calculate_value())