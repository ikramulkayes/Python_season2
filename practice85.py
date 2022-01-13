class Library:
    Total_book = 1000
    borrow_data = {}
    
    def __init__(self,n,id):
        self.student_name = n
        self.student_id = id     
    
    def borrowbook(self):
        print("A book is borrowed!")
        
    def __str__(self):
        return "Library: XYZ"

class Student(Library):
    
    def __init__(self, n, id):
        super().__init__(n, id)
        self.borrowlist = ""
    def __str__(self):
        return super().__str__()+f"\nStudent Name: {self.student_name} ID: {self.student_id}\nBooks borrowed: {self.borrowlist.rstrip(', ')}"
    def borrowbook(self,name,id=None):
        if name not in Library.borrow_data.keys():
            super().borrowbook()
            if id != None:
                print(f"'{name}' book with the unique id {id} is borrowed by {self.student_name}({self.student_id}")
                
            else:
                print(f"'{name}' book is borrowed by {self.student_name}({self.student_name})")
            Library.borrow_data[name] = [self.student_name]
            self.borrowlist += name + ", "
            Library.Total_book -= 1
            print(f"Number of books available for borrowing = {Library.Total_book}")
        else:
            print(f"Sorry {self.student_name} ! The Alchemist book is borrowed by {Library.borrow_data[name][0]}")
    def returnAllBooks(self):
        self.borrowlist =  self.borrowlist.rstrip(", ")
        temp = self.borrowlist.split(", ")
        for elm in temp:
            del Library.borrow_data[elm]
            #print(elm)
            #print(Library.borrow_data)
        print(f"All Books are returned by {self.student_name}.")
    

#Write your code here    
s1 = Student("Alice",18101259)
s1.borrowbook("The Alchemist", "Hdw652")
print("===============")
print(s1)
print("===============")
print(Library.borrow_data)
print("===============")
s1.borrowbook("Wuthering Heights")
print("===============")
print(s1)
print("===============")
s2= Student("David",18141777)
s2.borrowbook("The Alchemist", "Hdw652")
print("===============")
s2.borrowbook("The Vampyre")
print("===============")
print(Library.borrow_data)
print("===============")
s1.returnAllBooks()
print("===============")
print(Library.borrow_data)
