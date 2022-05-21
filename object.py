from parametres import Parametres

class Object(object):

    def __init__(self, weight: int = None, value:int = None):
        if not weight:
            self.weight = Parametres.random.randint(Parametres.OBJ_WEIGHT_MIN, Parametres.OBJ_WEIGHT_MAX)
        else:
            self.weight = weight
        
        if not value:
            self.value = Parametres.random.randint(Parametres.OBJ_VALUE_MIN, Parametres.OBJ_VALUE_MAX)
        else : 
            self.value = value

    def __str__(self) -> str:
        return 'Object - Weight : {} - Value : {} - Ratio : {}'.format(self.weight, self.value, self.value / self.weight)