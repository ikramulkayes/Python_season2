


loop = int(input("Enter a number: "))
wordlst = []
dic = {}
for elm in range(loop):
    k = input("Enter a name: ")
    wordlst.append(k)
    k = (k.split())
    if len(k) == 1:

        if "Fname" not in dic.keys():
            dic["Fname"] = []
    if len(k) == 3:
        if "Fname" not in dic.keys():
            dic["Fname"] = []
        if "Mname" not in dic.keys():
            dic["Mname"] = []
        if "Lname" not in dic.keys():
            dic["Lname"] = []
        
    else:
        if "Lname" not in dic.keys():
            dic["Lname"] = []
        if "Fname" not in dic.keys():
            dic["Fname"] = []

    

for elm in wordlst:
    elm = elm.split()
    if len(elm)==3:
        temp = dic["Fname"]
        temp.append(elm[0])
        dic["Fname"] = temp
        temp = dic["Mname"]
        temp.append(elm[1])
        dic["Mname"] = temp
        temp = dic["Lname"]
        temp.append(elm[2])
        dic["Lname"] = temp
    elif len(elm) == 2:
        temp = dic["Fname"]
        temp.append(elm[0])
        dic["Fname"] = temp
        temp = dic["Lname"]
        temp.append(elm[1])
        dic["Lname"] = temp
    else:
        temp = dic["Fname"]
        temp.append(elm[0])
        dic["Fname"] = temp

print(dic)





    

