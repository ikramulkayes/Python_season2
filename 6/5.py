class Employee:
    def __init__(self,name,year):
        self.name = name
        self.workingPeriod = year
    @classmethod
    def employeeByJoiningYear(cls,name,jyear):
        obj = cls(name,(2021-jyear))
        return obj
    @staticmethod
    def experienceCheck(year,gender):
        if year < 3:
            exp = "not experienced"
        else:
            exp ="experienced"
        if gender == "male":
            first = "He"
        else:
            first = "She"
        return f"{first} is {exp}"

employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))