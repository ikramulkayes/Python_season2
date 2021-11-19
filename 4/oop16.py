class Author:
    def __init__(self,*args):
        if len(args)==0:
            self.name = "Default"
            self.books = []
        elif len(args) == 1:
            self.name = args[0]
            self.books = []
        else:
            self.name = args[0]
            self.books = args[1::]
            self.books = list(self.books)
    def addBooks(self,*args):
        for elm in args:
            self.books.append(elm)
    def changeName(self,name):
        self.name = name
    def printDetails(self):
        print("Author Name:",self.name)
        print("--------")
        print("List of Books:")
        for elm in self.books:
            print(elm)


auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print("===================")
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print("===================")
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()