loop = int(input("Enter the number of lst you want to input: "))
lst = []
for elm in range(loop):
    word = input("Input your list: ")
    word = word.split()
    lst.append(word)

maxsum = None
maxlst = None
sum1 = 0
templst = []
for lstelm in lst:
    for elm in lstelm:
        elm = int(elm)
        templst.append(elm)
        sum1 += elm
    if maxsum == None:
        maxsum = sum1
        maxlst = templst
    elif sum1 > maxsum:
        maxsum = sum1
        maxlst = templst
    templst = []
    sum1 = 0
print(maxsum)
print(maxlst)

    