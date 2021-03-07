from abc import ABC, abstractmethod

class AbstractArticle(ABC):
    @abstractmethod
    def get_title(self):
        raise NotImplementedError("Calling method on abstract class")

    @abstractmethod
    def get_content(self):
        raise NotImplementedError("Calling method on abstract class")

    @abstractmethod
    def get_formulas(self):
        raise NotImplementedError("Calling method on abstract class")

    @abstractmethod
    def get_text(self):
        raise NotImplementedError("Calling method on abstract class")

    @abstractmethod
    def get_links(self):
        raise NotImplementedError("Calling method on abstract class")
