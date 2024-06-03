class Article:
    def __init__(self, author, magazine, title):
        self._author = None
        self._magazine = None
        self._title = None
        self.author = author
        self.magazine = magazine
  
        self.title = title
        

    @property
    def title(self):
        return self._title
       

    @title.setter
    def title(self,value):
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Title cannot be changed after the article is instantiated.")
        if isinstance(value, str)and 5<= len(value)<=50:
            self._title=value 
        else:raise ValueError("Title must be a string between 5 and 50 characters.")    
    @property
    def author(self):
        # if isinstance(self,Author):
        return self._author
    @author.setter
    def author(self,value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise ValueError("Author must be an instance of the Author class.")


        

    @property
    def magazine(self):
        # if isinstance(self, Magazine):
            return self._magazine
    @magazine.setter
    def magazine(self,value):
        if isinstance(value, Magazine):
            self._magazine = value
        else: raise ValueError("Magazine must be an instance of the Magazine class.")        

        
class Author:
    all =[]
    def __init__(self, name):
        if isinstance (name, str) and len(name)  > 0: 
            self._name = name
        else: 
            raise ValueError("Name must be a string greater than 0")
        self._articles=[]
        Author.all.append(all)

        @property
        def name(self):
            if hasattr(self , '_name'):
                return self._name
            else: return None    
        

    def articles(self):
        return self._articles

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    all =[]
    def __init__(self, name, category):


        if isinstance(name,str) and 2<=len(name) <= 16:
            self._name = name
        else: raise ValueError("Name must be a string between 2 -16 characters")

        if isinstance(category, str) and len(category) > 0:
            self.category = category
        else: 
            raise ValueError("Category must be a string with more than 0 characters")
        self._articles=[]
        
        # self.name = name
        # self.category = category

    @property 
    def name(self):
        return self._name
    

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len( value) > 0:
            self._category = value
        else: raise ValueError("Category must be a string with more than 0 characters")
    
    
    # @property
    # def category(self):
    #     return self.category

    # @name.setter
    # def name(self):
        

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass