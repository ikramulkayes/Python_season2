lst = []
while True:
    word = input("Enter your list: ")
    if word =="STOP":
        break
    else:
        word = word.split(" ")
        lst.append(word)
sum1 = 0
flag = True
count = 0
lim = 0
for lstelm in lst:
    for elm in lstelm:
        if count < len(lstelm) - 1:
            sum1 = int(elm) - int(lstelm[count+1])
            sum1 = abs(sum1)
            #print(sum1)
            count += 1
            if sum1 < len(lstelm) and sum1 > 0:
                continue
            else:
                flag = False
    if flag:
        print("UB Jumper")
            
    else:
        print("Not UB Jumper")
    flag = True
    count = 0
            
