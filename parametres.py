import random

class Parametres:
    MAX = 10
    NB_OBJ = 10000
    OBJ_WEIGHT_MAX = 5
    OBJ_WEIGHT_MIN = 1
    OBJ_VALUE_MAX = 9
    OBJ_VALUE_MIN = 1
    BAG_WEIGHT_MAX = OBJ_WEIGHT_MAX * NB_OBJ / 2.5
    POPULATION_SIZE = 20
    MAX_ITERATIONS = 10000
    MUTATION_PROP = .4
    MAX_MUTATION_COUNT = 3
    random = random

random.seed(1)