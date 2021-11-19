my_tuple = (("Mominul", 1101),("Mustafiz", 1202),("Bell", 2101),("Cook", 2103),("Smith", 3101),("Finch", 3102),("Starc", 3203), ("Imrul", 1103), ("Taijul", 1204))

dic = {}
for elm in my_tuple:
    num = str(elm[1])
    if num[0] == "1":
        if "Bangladesh" not in dic.keys():
            dic["Bangladesh"]= {}
        if num[1] == "1":
            if "Batters" not in dic["Bangladesh"].keys():
                dic["Bangladesh"]["Batters"] = [elm[0]]
            else:
                temp = dic["Bangladesh"]["Batters"]
                temp.append(elm[0])
                dic["Bangladesh"]["Batters"] = temp
        if num[1] == "2":
            if "Bowlers" not in dic["Bangladesh"].keys():
                dic["Bangladesh"]["Bowlers"] = [elm[0]]
            else:
                temp = dic["Bangladesh"]["Bowlers"]
                temp.append(elm[0])
                dic["Bangladesh"]["Bowlers"] = temp

    if num[0] == "2":
        if "England" not in dic.keys():
            dic["England"]= {}
        if num[1] == "1":
            if "Batters" not in dic["England"].keys():
                dic["England"]["Batters"] = [elm[0]]
            else:
                temp = dic["England"]["Batters"]
                temp.append(elm[0])
                dic["England"]["Batters"] = temp
        if num[1] == "2":
            if "Bowlers" not in dic["England"].keys():
                dic["England"]["Bowlers"] = [elm[0]]
            else:
                temp = dic["England"]["Bowlers"]
                temp.append(elm[0])
                dic["England"]["Bowlers"] = temp

    if num[0] == "3":
        if "Australia" not in dic.keys():
            dic["Australia"]= {}
        if num[1] == "1":
            if "Batters" not in dic["Australia"].keys():
                dic["Australia"]["Batters"] = [elm[0]]
            else:
                temp = dic["Australia"]["Batters"]
                temp.append(elm[0])
                dic["Australia"]["Batters"] = temp
        if num[1] == "2":
            if "Bowlers" not in dic["Australia"].keys():
                dic["Australia"]["Bowlers"] = [elm[0]]
            else:
                temp = dic["Australia"]["Bowlers"]
                temp.append(elm[0])
                dic["Australia"]["Bowlers"] = temp
#print(dic)
fdic = {}
tempdic = {}
for key, val in dic.items():
    #print(key)
    for k,v in val.items():
        if len(v) == 1:
            m = v[0]
            tempdic[k] = m
        else:
            temp = tuple(v)
            tempdic[k] = temp
    fdic[key] = tempdic
    #print(tempdic)
    tempdic = {}
print(fdic)