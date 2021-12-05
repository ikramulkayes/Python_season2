def arrangep(word):
    dic = {}
    for elm in word:
        name = elm[0]
        id = elm[1]
        id = str(id)
        dic[name] = id
    fdic = {}
    for k,v in dic.items():
        name = k
        cdigit = v[0]
        rdigit = v[1]
        county = ""
        role = ""
        if cdigit == "1":
            county = "Bangladesh"
        elif cdigit == "2":
            county = "England"
        elif cdigit == "3":
            county = "Australia"
        else:
            print("NO NO")
        if rdigit == "1":
            role = "Batters"
        elif rdigit == "2":
            role = "Bowlers"
        else:
            print("NO NO NO")
        if county not in fdic.keys():
            fdic[county] = {role:[k]}
        else:
            if role not in fdic[county].keys():
                fdic[county][role] = [name]
            else:
                temp = fdic[county][role]
                temp.append(name)
                fdic[county][role] = temp
    rdic = {}
    for k,v in fdic.items():
        rdic[k] = {}
        for a,b in v.items():
            if len(b)>1:
                rdic[k][a] = tuple(b)
            else:
                rdic[k][a] = b[0]
        


    return rdic
print(arrangep((("Mominul", 1101),("Mustafiz", 1202),("Bell", 2101),("Cook",
2103),("Smith", 3101),("Finch", 3102),("Starc", 3203), ("Imrul", 1103),
("Taijul", 1204))))
        

        

