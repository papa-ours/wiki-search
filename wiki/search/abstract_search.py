from abc import ABC, abstractmethod
from ..article.abstract_article import AbstractArticle

class AbstractSearch(ABC):
    def __init__(self, limit: int = 50):
        self.limit = limit
    
    @abstractmethod
    def execute(self) -> AbstractArticle:
        raise NotImplementedError("Calling method on abstract class")
