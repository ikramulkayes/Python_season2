def iddevider(word):
    word = word.split()
    lst = []
    dic = {}
    for elm in word:
        gg = elm[0:2] + "th"
        if gg not in dic.keys():
            dic[gg] = [elm]
        else:
            temp = dic[gg]
            temp.append(elm)
            dic[gg] = temp
    print(dic)

iddevider("18466 194544 18454545 2044646")
        

        