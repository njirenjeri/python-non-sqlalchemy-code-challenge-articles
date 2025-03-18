class Article:

    all_articles = []

    def __init__(self, author, magazine, title):


        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or not(5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all_articles.append(self)

        @property
        def title(self):
            return self._title

        @property
        def author(self):
            return self._author
        
        @author.setter
        def author(self, value):
            if not isinstance(value, Author):
                raise ValueError("Author must be an instance of Author")
            self._author = value
        
        @property
        def magazine(self):
            return self._magazine 
        
        @magazine.setter
        def magazine(self, value):
            if not isinstance(value, Magazine):
                raise ValueError("Magazine must be an instance of Magazine")
            self._magazine = value


        
class Author:
    def __init__(self, name):

        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        
        self.name = name

        @property
        def name(self):
            return self.name

    def articles(self):
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list(set(mag.category for mag in self.magazines()))
        return categories if categories else None

class Magazine:

    all_magazines = []

    def __init__(self, name, category):

        if not isinstance(name, str) or not (2<= len(name) <= 16):
            raise ValueError('Name must be a string between 2 and 16 characters')
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("category must be a non-empty string")

        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string of between 2 and 16 Characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value


    def articles(self):
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        # return [article.title for article in self.articles()]
        titles = [article.title for article in self.articles() if hasattr(article, 'title')]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        return [author for author in set(authors) if authors.count(author) > 2] or None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all_articles:
            return None
        return max(cls.all_magazines, key = lambda mag: len(mag.articles()))