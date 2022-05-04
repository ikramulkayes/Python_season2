word = input("Enter a string: ")
word = word.split(", ")
hnum = 0
dic = {}
for elm in word:
    elm = int(elm)
    if hnum == 0:
        hnum = elm
    elif hnum < elm:
        hnum = elm
print(hnum)
for elm in word:
    flag = True
    for i in range(2,hnum//2):
        elm = int(elm)
        if elm%i==0:
            flag = False
            if i not in dic.keys():
                dic[i] = [elm]
            else:
                temp = dic[i]
                temp.append(elm)
                dic[i] = temp
    if flag:
        if "None"not in dic.keys():
            dic["None"] = [elm]
        else:
            temp = dic["None"]
            temp.append(elm)
            dic["None"] = temp
        
print(dic)