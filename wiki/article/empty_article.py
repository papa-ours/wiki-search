from .abstract_article import AbstractArticle

class EmptyArticle(AbstractArticle):
    def __init__(self):
        self.title = ""
        self.content = ""

    def get_title(self):
        return self.title
    
    def get_content(self):
        return self.content
    
    def get_formulas(self):
        return []
    
    def get_text(self):
        return ""
        
    def get_links(self):
        return []
