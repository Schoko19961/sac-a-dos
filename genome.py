from abc import ABC, abstractmethod

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
    def create_child(pere):
        pass
