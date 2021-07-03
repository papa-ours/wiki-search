from .abstract_search import AbstractSearch

from ..article.abstract_article import AbstractArticle
from ..article.article import Article
from ..article.empty_article import EmptyArticle
from ..article.collection import Collection
from ..common.ressource import Ressource

import requests
from multiprocessing import Pool
from functools import partial
from enum import Enum

class CategorySearch(AbstractSearch):
    PREFIX = "Category:"    
    
    class Type(Enum):
        SUB_CAT = "subcat"
        PAGE = "page"
    
    @staticmethod
    def get_category_name(category_name: str):
        if category_name.startswith(CategorySearch.PREFIX):
            return category_name
        
        return CategorySearch.PREFIX + category_name
    
    def __init__(self, category_name: str, limit: int = 50, max_depth: int = 3):
        self.category_name = CategorySearch.get_category_name(category_name)
        self.max_depth = max_depth
        super().__init__(limit)
        
    def create_category(self, member: dict, depth: int) -> AbstractArticle:
        if member["type"] == CategorySearch.Type.SUB_CAT.value:
            return CategorySearch(member["title"], self.limit).execute(depth + 1)
        elif member["type"] == CategorySearch.Type.PAGE.value:
            return Article(member["title"])

        return EmptyArticle()
    
    def execute(self, depth = 0) -> Collection:
        if depth > self.max_depth:
            return Collection([])
        
        params = {
            "action": "query",
            "cmlimit": self.limit,
            "format": "json",
            "list": "categorymembers",
            "cmtitle": self.category_name,
            "cmprop": "title|type",
        }
        response = requests.get(Ressource.API_URL, params = params)
        if response.status_code == 200:
            data = response.json()
            
            try:
                members = data["query"]["categorymembers"]
                
                try:
                    with Pool(processes=8) as p:
                        f = partial(self.create_category, members)
                        
                        return Collection(p.map(f, depth))
                except:
                    # Use list comprehension if multiprocessing failed
                    return Collection([self.create_category(member, depth) for member in members])
            except:
                return Collection([])
           
        return Collection([])
