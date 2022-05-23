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
        # 1 pour avoir au moins une partie du genome de la mère & -2 pour avoir au moins une partie du genome du père
        mere_size = Parametres.random.randint(1, Parametres.NB_OBJ - 2)
        # Prends une partie du genome de la mère et du père et assemble-les
        new_genome = self.genome[:mere_size] + father.genome[mere_size:]
        # Creation d'un nouveau sac à dos avec le nouveau genome.
        child = Bag(self.objects, new_genome)
        # Lance la mutation
        child.mutate()
        return child

    def mutate(self):
        # Choisir au hasard s'il y a une mutation
        mutate_factor = Parametres.random.random()
        if mutate_factor > Parametres.MUTATION_PROP:
            pass
        # Choisir au hasard la quantité des mutations
        mutation_count = Parametres.random.randint(1, Parametres.MAX_MUTATION_COUNT)
        for _ in range(mutation_count):
            # Choisir au hasard le type de mutation
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
        # Choissisez le type d'evalutation
        return self.evaluate1()
        # return self.evaluate2()
        # return self.evaluate3()

    # Algorithme Evaluation 1: ajoute la valeur au fitness et supprime le poid.
    def evaluate1(self) -> float:
        value = self.calculate_value()
        weight = self.calculate_weight()
        # Sie le poid est trop grand, le fitness est 0
        if(weight > Parametres.BAG_WEIGHT_MAX):
            self.fitness = 0
        else:
            self.fitness = value - weight
        return self.fitness

    # Algorithme Evaluation 2: N'ajoute que la valeur au fitness
    def evaluate2(self) -> float:
        value = self.calculate_value()
        weight = self.calculate_weight()
        # Sie le poid est trop grand, le fitness est 0
        if(weight > Parametres.BAG_WEIGHT_MAX):
            self.fitness = 0
        else:
            self.fitness = value
        return self.fitness
    
    # Algorithme Evaluation 3: Ajoute la valeur et le ratio de valeur / poid au fitness.
    def evaluate3(self) -> float:
        value = self.calculate_value()
        weight = self.calculate_weight()
        # Sie le poid est trop grand, le fitness est 0
        if(weight > Parametres.BAG_WEIGHT_MAX):
            self.fitness = 0
        else:
            self.fitness = value + value / weight * sum(self.genome)
        return self.fitness


    def __str__(self) -> str:
        return '[{}] Bag - Items : {} - Weight : {}/{} - Value : {}'.format(self.evaluate(), sum(self.genome), self.calculate_weight(), Parametres.BAG_WEIGHT_MAX ,self.calculate_value())