loop = int(input("Enter number of inputs: "))
lst = []
for elm in range(loop):
    k = input("Enter a name: ")
    lst.append(k)

dic = {}

for elm in lst:
    elm = elm.split(" ")
    if len(elm) == 1:
        if "Fname" not in dic.keys():
            dic["Fname"] = [elm[0]]
        else:
            temp = dic["Fname"]
            temp.append(elm[0])
            dic["Fname"] = temp
    elif len(elm) == 2:
        
        count = 0
        for k in ["Fname","Lname"]:
            if k not in dic.keys():
                dic[k] = [elm[count]]
            else:
                temp = dic[k]
                temp.append(elm[count])
                dic[k] = temp
            count += 1
    elif len(elm) == 3:
        
        count = 0
        for k in ["Fname","Mname","Lname"]:
            if k not in dic.keys():
                dic[k] = [elm[count]]
            else:
                temp = dic[k]
                temp.append(elm[count])
                dic[k] = temp
            count += 1
print(dic)
    



