from .abstract_article import AbstractArticle

from collections.abc import Iterable
from typing import List, Union

class Collection(AbstractArticle):
    @staticmethod
    def flatten(elements):
        for element in elements:
            if isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
                yield from Collection.flatten(element)
            else:
                yield element
    
    def __init__(self, articles: List[AbstractArticle] = []):
        self.__articles = articles
    
    def add(self, to_add: Union[AbstractArticle, List[AbstractArticle]]):
        if isinstance(to_add, Iterable):
            self.__articles.append(Collection(to_add))
        else:
            self.__articles.append(to_add)
            
    def get_articles(self):
        return self.__articles
        
    def get_title(self):
        return [article.get_title() for article in self.__articles]
    
    def get_content(self):
        return [article.get_content() for article in self.__articles]
    
    def get_formulas(self):
        return [article.get_formulas() for article in self.__articles]
    
    def get_text(self):
        return [article.get_text() for article in self.__articles]
        
    def get_links(self):
        return [article.get_links() for article in self.__articles]
