times = int(input())
lst = []
for elm in range(times):
    k = input()
    lst.append(k)
temp = ""
ftemp = ""

for belm in lst:
    count = 1
    flag = True
    ftemp = ""
    temp = ""
    for elm in belm:
        if temp == "" and elm !="B" and flag:
            temp = elm
            flag = False
        elif elm !="B":
            temp += elm
        elif elm == "B" and flag == False:
            temp += elm
            ftemp += temp
            temp = ""
            flag = True
        count += 1
    #print(ftemp)
    if belm[-1] == "B" and belm == ftemp:
        print("Yes")
    else:
        print("No")

        
        
        

