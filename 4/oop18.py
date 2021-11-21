class Student:
    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept = dept
        self.lst = []
        self.final = ""
    def details(self):
        print("Name:",self.name)
        print("ID:",self.id)
        return f"Department:{self.dept}"
    def advise(self,*args):
        for elm in args:
            self.lst.append(elm)
            self.final += elm +", "
        self.final = self.final.rstrip(", ")
        print(f"{self.name}, you have taken {(len(self.lst))*3.0} credits.")
        print("List of courses:",self.final)
        if len(self.lst)>2 and len(self.lst)<5:
           
           
            print("Status: Ok")
        else:
            if len(self.lst) <3:
               print(f"Status: You have to take at least {3-len(self.lst)} more course.")
            else:
                print(f"Status: You have to drop at least {len(self.lst) - 4} course.")


s1 = Student('Alice','20103012','CSE')
s2 = Student('Bob', '18301254','EEE')
s3 = Student('Carol', '17101238','CSE')
print('##########################')
print(s1.details())
print('##########################')
print(s2.details())
print('##########################')
s1.advise('CSE110', 'MAT110', 'PHY111')
print('##########################')
s2.advise('BUS101', 'MAT120')
print('##########################')
s3.advise('MAT110', 'PHY111', 'ENG102',
'CSE111', 'CSE230')
