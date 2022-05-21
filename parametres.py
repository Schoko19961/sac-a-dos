import random


class Parametres:
    NB_OBJ = 5000
    OBJ_WEIGHT_MAX = 10
    OBJ_WEIGHT_MIN = 1
    OBJ_VALUE_MAX = 15
    OBJ_VALUE_MIN = 5
    BAG_WEIGHT_MAX = OBJ_WEIGHT_MAX * NB_OBJ / 3
    POPULATION_SIZE = 20
    MAX_ITERATIONS = 7500
    MUTATION_PROP = .4
    MAX_MUTATION_COUNT = 3
    random = random

random.seed(1)