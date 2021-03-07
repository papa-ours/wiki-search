from ..article.article import Article
from .abstract_search import AbstractSearch
from ..common.ressource import Ressource

from multiprocessing import Pool
import requests

class ArticleSearch(AbstractSearch):
    
    def __init__(self, search_term, limit = 50):
        self.search_term = search_term
        super().__init__(limit)
        
    def create_article(self, title):
        return Article(title)
        
    def execute(self):
        params = {
            "action": "opensearch",
            "limit": self.limit,
            "format": "json",
            "search": self.search_term,
        }
        response = requests.get(Ressource.API_URL, params = params)
        if response.status_code == 200:
            data = response.json()
            
            try:
                with Pool(processes=8) as p:
                    return p.map(self.create_article, data[1])
            except:
                # Use list comprehension if multiprocessing failed
                return [self.create_article(title) for title in data[1]]
                
        return []
