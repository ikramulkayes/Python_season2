lst = input("Enter you dictionary: ")
lst = lst[1:-1]
lst = lst.split(",")
dic = {}
for elm in lst:
    elm = elm.lstrip(" '")
    elm = elm.rstrip("'")
    year ="20"+ elm[0:2]
    deptcode = elm[3:5]
    print(deptcode)
    if deptcode == "01":
        dept = "CSE"
    elif deptcode == "41":
        dept = "CS"
    elif deptcode=="21":
        dept = "EEE"
    else:
        dept = "Other"
    if year not in dic.keys():
        dic[year] = {dept:[elm]}
    else:
        if dept not in dic[year].keys():
            dic[year][dept] = [elm]
        else:
            temp = dic[year][dept]
            temp.append(elm)
            dic[year][dept] = temp
final = {}
for key,val in dic.items():
    temp = {}
    for k,v in val.items():
        temp[k] = tuple(v)
    final[key] = temp
print(final)
#print(dic)
        
