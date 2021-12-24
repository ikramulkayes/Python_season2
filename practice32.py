loop = int(input("Enter times: "))
lst = []
flst = []
vcount = 0
incount = 0
for elm in range(loop):
    num = int(input("Enter your marks: "))
    lst.append(num)
for elm in lst:
    if elm <101 and elm >0:
        flst.append(elm)
        vcount += 1
    else:
        incount += 1
error = incount /len(lst)
average = sum(flst) / vcount
print(average)
print(error*100)
