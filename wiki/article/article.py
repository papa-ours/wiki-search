from .abstract_article import AbstractArticle
from ..common.ressource import Ressource

import requests
import re

class Article(AbstractArticle):
    def __init__(self, title):
        self.title = title
        self.content = self.__get_content()

    def get_title(self):
        return self.title
    
    def get_content(self):
        return self.content
    
    def get_formulas(self):
        return re.findall(r"<math>.*?</math>", self.content, flags=re.DOTALL)
    
    def get_text(self):
        return re.sub(r"<math>.*?</math>", "", self.content, flags=re.DOTALL)
        
    def get_links(self):
        return re.findall(r"\[\[.*?\]\]", self.content, flags=re.DOTALL)
    
    def __get_content(self):
        params = {
            "action": "query",
            "prop": "revisions",
            "rvprop": "content",
            "format": "json",
            "titles": self.title,
        }
        response = requests.get(Ressource.API_URL, params = params)
        try:
            if response.status_code == 200:
                data = response.json()
                pages = data["query"]["pages"]

                return pages[next(iter(pages.keys()))]["revisions"][0]["*"]
        except:
            pass
    
        return ""
