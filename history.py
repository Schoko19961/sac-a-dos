from bag import Bag


class History(object):

    def __init__(self, genome: Bag) -> None:
        self.fitness = genome.fitness
        self.value = genome.calculate_value()
        self.weight = genome.calculate_weight()
        self.ratio = self.value / self.weight
        self.items = sum(genome.genome)
        