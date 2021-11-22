class Author:
    def __init__(self,name=None):
        self.name = name
        self.dic = {}
        self.count = 0
    def addBook(self,bname,genere):
        if self.name == None:
            print("A book can not be added without author name")
        else:
            if genere not in self.dic.keys():
                self.dic[genere] = bname +","
            else:
                self.dic[genere] += bname +","
            self.count += 1
    def setName(self,name):
        self.name = name
    def printDetail(self):
        print("Number of Book(s):",self.count)
        print("Author Name:",self.name)
        for k,v in self.dic.items():
            print(k+": "+v.rstrip(", "))


a1 = Author()
print("=================================")
a1.addBook('Ice', 'Science Fiction')
print("=================================")
a1.setName('Anna Kavan')
a1.addBook('Ice', 'Science Fiction')
a1.printDetail()
print("=================================")
a2 = Author('Humayun Ahmed')
a2.addBook('Onnobhubon', 'Science Fiction')
a2.addBook('Megher Upor Bari', 'Horror')
print("=================================")
a2.printDetail()
a2.addBook('Ireena', 'Science Fiction')
print("=================================")
a2.printDetail()
print("=================================")