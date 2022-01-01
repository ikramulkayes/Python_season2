class University:
    name  = "ABC University"
    numberOfStudents = 0
    admissionFee = 28000
    Library = 2000

    def __init__(self, n,i):
        self.stName = n
        self.stId = i
             
    def payment(self):

        return self.admissionFee + self.Library

    def __add__(self,other):
        sum1 = self.prevfee + other.prevfee
        return sum1
    def __str__(self):
        return "Student Name: {}, ID: {}\nFee: {}".format(self.stName, self.stId, self.payment())

# Write your codes here.
# Do not change the following lines of code.
class CSE_dept(University):
	PerCreditFee = 6600
	SemesterFee = 7700
	LabFee = 2750
	

	def __init__(self, n, i,credits = 6):
		super().__init__(n, i)
		self.credits = credits
		self.prevfee = 0
		University.numberOfStudents += 1

	def payment(self):
		self.prevfee= super().payment()
		self.prevfee += CSE_dept.PerCreditFee*self.credits+CSE_dept.SemesterFee+CSE_dept.LabFee
		
		return self.prevfee
	def __str__(self):
		return super().__str__()
	def payment_details(self):
		print(f"Admission Fee: {self.admissionFee}")
		print(f"Library Fee: {CSE_dept.Library}")
		print(f"Semester Fee: {CSE_dept.SemesterFee}")
		print(f"Per Credit Fee: {CSE_dept.PerCreditFee}")
		print(f"Number of credits: {self.credits}")
		print(f"Lab Fee:",CSE_dept.LabFee)

class PHR_dept(University):
	PerCreditFee = 6600
	SemesterFee = 11000
	
	

	def __init__(self, n, i,credits = 9):
		super().__init__(n, i)
		self.credits = credits
		University.numberOfStudents += 1
		self.prevfee = 0

	def payment(self):
		self.prevfee= super().payment()
		self.prevfee += PHR_dept.PerCreditFee*self.credits+PHR_dept.SemesterFee
		
		return self.prevfee
	def __str__(self):
		return super().__str__()
	def payment_details(self):
		print(f"Admission Fee: {self.admissionFee}")
		print(f"Library Fee: {PHR_dept.Library}")
		print(f"Semester Fee: {PHR_dept.SemesterFee}")
		print(f"Per Credit Fee: {PHR_dept.PerCreditFee}")
		print(f"Number of credits: {self.credits}")


	
	


c1 = CSE_dept("Mary","5678")  
print(c1)
c1.payment_details()
print("===========================")
p1 = PHR_dept("Simon","91011")  
print(p1)
p1.payment_details()
print("===========================")
c2 = CSE_dept("Adam","1234", 12)  
print(c2)
c2.payment_details()
print("===========================")
p2 = PHR_dept("David","121314", 15)  
print(p2)
p2.payment_details()
print("===========================")
print("Total Number of Students:", University.numberOfStudents)
print("Total University Revenue:", (c1 + c2) + (p1 + p2))
print("===========================")
print("Due to the pandemic, admission and library fees have been reduced for all departments. ")
University.admissionFee -= 1000
University.Library -= 100
print("The credit, semester and lab fees have been reduced for the CSE department. ")
CSE_dept.PerCreditFee -= 100
CSE_dept.SemesterFee -= 100
CSE_dept.LabFee -=100
print("The credit and semester fees have been reduced for the PHR department.\n ")
PHR_dept.PerCreditFee -= 100
PHR_dept.SemesterFee -= 1000
print(c1)
print(p1)
print(c2)
print(p2)
print("===========================")
print("Total Number of Students:", University.numberOfStudents)
print("Total University Revenue:", (c1 + c2) + (p1 + p2))