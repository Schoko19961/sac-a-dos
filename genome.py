from abc import ABC, abstractmethod
from typing_extensions import Self

# Classe abstracte pour le genome. Définit que le génome est un tableau et les fonctions obligatoires.
class Genome(ABC):
    def __init__(self, genome = []) -> None:
        super().__init__()
        self.fitness = -1
        self.genome = genome

    @abstractmethod
    def mutate(self) -> None:
        pass
    
    @abstractmethod
    def evaluate(self) -> float:
        pass

    @abstractmethod
    def create_child(father: Self) -> Self:
        pass
