def function_name(word):
    lst = []
    numcount = 0
    lcount = 0
    numlst = []
    llst = []
    flag = True
    for elm in word:
        if elm.isalpha():
            lcount += 1
            llst.append(elm)
        elif elm.isdigit():
            numcount += 1
            numlst.append(elm)
    if numcount >= lcount:
        times = numcount // lcount +1
    else:
        times = lcount//numcount + 1
        flag = False
        if lcount%numcount !=0:
            flag = True
    
    print(numcount,lcount)
    numcount = 0
    lcount = 0  
    print(times)
    for i in range(1,len(word)):
        if flag:
            if i%times == 0:
                lst.append(llst[lcount])
                lcount += 1
            else:
                lst.append(numlst[numcount])
                numcount += 1
        else:

            if i%times != 0:
                lst.append(llst[lcount])
                lcount += 1
            else:
                lst.append(numlst[numcount])
                numcount += 1           
        if len(llst) <=lcount or len(numlst) <= numcount:
            break
    if len(llst) >lcount:
        lst = lst + llst[lcount::]
    elif len(numlst) > numcount:
        lst = lst + numlst[numcount::]
        
    return lst

print(function_name(['2', '6', 't', '5', 'a', 'd', 's', 'f', '7', 'i', 'j', '9', 'a', '4', 'b']))


