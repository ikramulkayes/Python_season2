class myList:
    def __init__(self,*args):
        self.lst = args
        self.lst = list(self.lst)
    def merge(self,*args):
        for elm in args:
            self.lst.append(elm)
    def sum(self):
        sum1 = sum(self.lst)
        print(f"Sum: {sum1}")
    def average(self):
        if len(self.lst)>1:
            avg = sum(self.lst)/len(self.lst)
            print(f"Average: {avg}")
        else:
            print(f"Average: 0")
    






l1 =  myList(2,3,4,5,6) #you might need a list inside your class to store the values
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print("-----------------------------")
l2 =  myList()
l2.average()
l2.merge(1,2,4,8)
l2.sum()
