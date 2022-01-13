class MarketingDepartmentEmployee:
    employeeInfo = {}
    def __init__(self, name, designation, workHour): #workHour = Per week working hour
        self.name = name
        self.designation = designation
        self.workHour = workHour

    def calculateWeeklyIncome(self):
        pass

    def __str__(self):
        s = f"Name: {self.name}\nDesignation: {self.designation}\nWork hour per week: {self.workHour} hours"
        return s

#Write your code here
class MarketingOfficer(MarketingDepartmentEmployee):
    def __init__(self, name, designation, workHour,perhourincome,overtime=0):
        super().__init__(name, designation, workHour)
        self.perhourincome = perhourincome
        self.overtime = overtime
        print(f"{self.designation} {self.name} - created.")
        if self.designation not in MarketingDepartmentEmployee.employeeInfo.keys():
            MarketingDepartmentEmployee.employeeInfo[self.designation] = [self.name]
        else:
            temp = MarketingDepartmentEmployee.employeeInfo[self.designation]
            temp.append(self.name)
            MarketingDepartmentEmployee.employeeInfo[self.designation] = temp
    def calculateWeeklyIncome(self):
        print(f"Weekly income of {self.name} has been calculated")
        self.weeklyincome = (self.workHour+self.overtime)*self.perhourincome
    def __str__(self):
        print(super().__str__())
        s = ""
        s+= f"Per hour income: {self.perhourincome} Taka\n"
        s+= f"Over time:{self.overtime} hours\n"
        s += f"Weekly income: {self.weeklyincome} Taka\n"
        return s.rstrip("\n")


class CommunicationOfficer(MarketingOfficer):
    def __init__(self, name, designation, workHour, perhourincome, overtime=0):
        super().__init__(name, designation, workHour, perhourincome, overtime=overtime)


# Do not change the following lines of code.
cm1 = MarketingOfficer("Ross","Chief Marketing Officer",45,1500)
print('1.------------------------------------')
cm1.calculateWeeklyIncome()
print('2.------------------------------------')
print(cm1)
print('3.------------------------------------')
cm2 = MarketingOfficer("Rachel","Chief Marketing Officer",45,2000,5)
print('4.------------------------------------')
cm2.calculateWeeklyIncome()
print('5.------------------------------------')
print(cm2)
print('6.------------------------------------')
print(MarketingDepartmentEmployee.employeeInfo)
print('7.====================================')
co1 = CommunicationOfficer("Chandler","Communication Officer",50,1000,7)
print('8.------------------------------------')
co1.calculateWeeklyIncome()
print('9.------------------------------------')
print(co1)
print('10.------------------------------------')
co2 = CommunicationOfficer("Monica","Chief Communication Officer",55,1200)
print('11.------------------------------------')
co2.calculateWeeklyIncome()
print('12.------------------------------------')
print(co2)
print('13.------------------------------------')
print(MarketingDepartmentEmployee.employeeInfo)