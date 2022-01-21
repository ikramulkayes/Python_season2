#Write your code here
class Library:
    def __init__(self,name):
        self.name = name
        self.lst = []
    def addBook(self,*args):
        for elm in args:
            if elm.isbn != None:
                self.lst.append(f"Book name:{elm.name} Writer:{elm.author} ISBN no:{elm.isbn}")
                print(f"Book with ISBN: {elm.isbn} added")
            else:
                print("A book without ISBN cannot be added.")
    def printBooks(self):
        for elm in self.lst:
            print(elm)
    
class Book:
    def __init__(self,name,author,isbn=None):
        self.name = name
        self.author = author
        self.isbn = isbn
    def setISBN(self,isbn):
        self.isbn = isbn




#========================================================================================
# Do not change the codes below
obj = Library("Ayesha Abed Library")
b1 = Book("Teach yourself C","Herbet Schildt","0078823110")
print("=================================")
obj.addBook(b1)
print("=================================")
obj.printBooks()
print("=================================")
b2 = Book("Java:How to program","Deitel & Deitel")
b3 = Book("Python Crash Course","Eric Hatthes","1593279280")
print("=================================")
obj.addBook(b2,b3)
print("=================================")
obj.printBooks()
print("=================================")
b2.setISBN("0134791401")
print("=================================")
obj.addBook(b2)
print("=================================")
obj.printBooks()
print("=================================")
b4 = Book("Automate the boring stuff with Python","Al Sweigart","1593279922")
b5 = Book("Teach yourself C++","Herbet Schildt","0078820251")
print("=================================")
obj.addBook(b4,b5)
print("=================================")
obj.printBooks()
print("=================================")