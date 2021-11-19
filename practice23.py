word = input("Enter your string: ")
dic = {}
length = len(word)
count = 0
lcount = 2
while True:
    
    for elm in range(count,length):
        if lcount >length:
            break
        temp = word[count:lcount]
        if len(temp)%2 == 0:
            atemp = temp[0:(len(temp)//2)]
            btemp = temp[(len(temp)//2)::]
            acount = atemp.count("A")
            bcount = btemp.count("B")
            #print(count)
            #print(lcount)
            #print(atemp)
            
            #print(btemp)
            #print("--------")
            
            if acount == bcount and acount == len(atemp) and bcount == len(btemp):
                if temp not in dic.keys():
                    dic[temp] = 1
                else:
                    k = dic[temp]
                    k += 1
                    dic[temp] = k
            else:
                acount = atemp.count("B")
                bcount = btemp.count("A")
                if acount == bcount and acount == len(atemp) and bcount == len(btemp):
                    if temp not in dic.keys():
                        dic[temp] = 1
                    else:
                        k = dic[temp]
                        k += 1
                        dic[temp] = k
        lcount += 1
    count += 1
    lcount = count + 2
    if count >= length:
        break
print(dic)
maxseq = None
maxnum = None

for key,val in dic.items():
    if maxnum == None:
        maxseq = key
        maxnum = len(key)
    elif len(key) > maxnum:
        maxseq = key
        maxnum = len(key)
    print(f"{key} - {val} times")
print("Longest Pattern -",maxseq)
            