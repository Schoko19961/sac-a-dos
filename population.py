import math
from typing import List
from genome import Genome
from parametres import Parametres


class Population(object):
    def __init__(self, population: List[Genome]) -> None:
        self.population = population
        self.best = self.population[0]
        self.iteration = 0
    
    def run(self) -> None:
        for iteration in range(Parametres.MAX_ITERATIONS):
            self.population.sort(key=lambda bag: bag.fitness)
            # Print new bag if better one was found
            if self.best.fitness < self.population[0].fitness:
                print(self.population[0])
            
            self.best = self.population[0]
            self.iteration = iteration

            # Print every 100 iterations
            if iteration % 100 == 0:
                print(self)


            new_population = [self.selection().create_child(self.selection()) for _ in range(Parametres.POPULATION_SIZE - 1)]
            new_population.append(self.best)
            self.population = new_population

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
        return "**** Iteration {} ****\n{}".format(self.iteration, self.best.fitness)


    