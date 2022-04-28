from abc import ABC, abstractmethod

class Genome(ABC):
    def __init__(self) -> None:
        self.fitness = -1
        super().__init__()

    @abstractmethod
    def mutate(self) -> None:
        pass
    
    @abstractmethod
    def evaluate(self) -> float:
        pass

    @abstractmethod
    def create_child(pere):
        pass
