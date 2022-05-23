import math
from typing import List
from genome import Genome
from parametres import Parametres


class Population(object):
    def __init__(self, population: List[Genome]) -> None:
        self.population = population
        self.best = self.population[0]
        self.history: List[Genome] = []
    
    def run(self) -> None:
        for iteration in range(Parametres.MAX_ITERATIONS):
            # Fait l'évalutaion pour tous les genomes dans la population.
            for genome in self.population:
                genome.evaluate()
            # Trier selon le fitness.
            self.population.sort(key=lambda genome: genome.fitness, reverse=True)
            # Imprimer le meilleur genome si un nouveau est trouvé
            if self.best.fitness < self.population[0].fitness:
                self.best = self.population[0]
                print(self)
            # Ajoute le meilleure genome à l'histoire
            self.history.append(self.best)
            # Imprimer la population tout les 100 iterations.
            if (iteration + 1) % 100 == 0:
                print(self)
            # Fait une nouvelle population bases sur le principe mère-père.
            new_population = [self.selection().create_child(self.selection()) for _ in range(Parametres.POPULATION_SIZE - 1)]
            new_population.append(self.best)
            self.population = new_population
        print(self)

    def selection(self) -> Genome:
        list_len = len(self.population)
        totalRanks = math.floor(list_len * (list_len + 1) / 2)
        rand = Parametres.random.randint(0, totalRanks -1)
        indIndex = 0
        nbParts = list_len
        totalParts = 0
        while totalParts <= rand:
            indIndex += 1
            totalParts += nbParts
            nbParts -= 1
        indIndex -=1
        return self.population[indIndex]

    def __str__(self) -> str:
        ret_str = "**** Iteration {} -> fitness: {} ****\n{}".format(len(self.history), self.best.fitness, self.best)
        return ret_str


    