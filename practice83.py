class myList:
    count = 0
    sumvar = 0
    averagevar = 0

    def __init__(self,*args):
        self.lst = args
        myList.count += len(args)
        
        for elm in self.lst:
            myList.sumvar+= elm
    def sum(self):

        print("Sum:",myList.sumvar)
    def average(self):
        if myList.count !=0:
            myList.average = myList.sumvar/myList.count
        print("Average:",myList.average)
    def merge(self,*args):
        for elm in args:
            myList.sumvar += elm
        myList.count += len(args)

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

        

        