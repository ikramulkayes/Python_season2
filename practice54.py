


inp=input("")
lst_0=[]
dict={}
lst_y=[]
for i in inp:
    lst_0.append(i)
for j in range(0,len(lst_0)):
    cnt=0
    for k in lst_0:
        if lst_0[j]==k:
            cnt+=1
            dict[lst_0[j]]=cnt
largest = 0
ltime = 0
second = 0
stime = 0
for k,v in dict.items():
    print(k)
    print(v)
    print("--------")
    if largest == 0:
        largest = k
        ltime = v

    elif v > ltime:
        second = largest
        stime = ltime
        largest = k
        ltime = v
    print(largest)
    print(second)

print(dict)
if second == 0:
    prevval = 0
    flag = True
    lst = []
    for k,v in dict.items():
        if prevval == 0:
            prevval = v
        elif prevval != v:
            flag = False
        lst.append(k)
    if flag:
        print("The word has all characters only once")
    else:
        for elm in lst:
            if elm != largest:
                print(elm)
                break

    
else:
    
    print(second)



    
    



