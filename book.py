class Book:
    def __init__(self,name,author,pages):
        self.name = name
        self.author = author
        self.pages = pages
        
    def summary(self):
        print(f"{self.name} by {self.author} wrote {self.pages}")
        
b1 = Book("G","GG",300)

b1.summary()