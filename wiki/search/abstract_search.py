from abc import ABC, abstractmethod

class AbstractSearch(ABC):
    def __init__(self, limit = 50):
        self.limit = limit
    
    @abstractmethod
    def execute(self):
        raise NotImplementedError("Calling method on abstract class")
