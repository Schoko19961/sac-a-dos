from typing import List
from bag import Bag

from object import Object
from parametres import Parametres


class Population(object):
    def __init__(self, objects: List[Object]) -> None:
        self.population = [Bag(objects) for _ in range(Parametres.POPULATION_SIZE)]

    