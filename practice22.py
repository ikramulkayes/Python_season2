dic = {}
for elm in range(10):
    word = input("Enter your player data: ")
    word = word.split()
    count = 0
    for i in word:
        if count ==0:
            dic[word[1]] = []
        if count >1:
            i = int(i)
            temp = dic[word[1]]
            temp.append(i)
            dic[word[1]] = temp
        count += 1
scoredic = {}
for key,val in dic.items():
    temp = []
    count = 0
    for elm in val:
        if count ==0 or count == 3:
            elm = elm*2
            temp.append(elm)
        if count == 2:
            temp.append(elm)
        if count == 4:
            elm = elm*3
            temp.append(elm)
        if count == 5:
            elm = elm*-1
            temp.append(elm)
        count += 1
    scoredic[key] = sum(temp)
print(scoredic)
maxcount = None
maxplayer = None
count = 0
for elm in range(3):
    maxcount = None
    maxplayer = None
    for key,val in scoredic.items():
        if maxcount == None:
            maxplayer = key
            maxcount = val
        elif val > maxcount:
            maxplayer = key
            maxcount = val
    if count == 0:
        print("First:",maxplayer)
    elif count == 1:
        print("Second:",maxplayer)
    elif count == 2:
        print("Third:",maxplayer)
        break
    del scoredic[maxplayer]
    count += 1
    

