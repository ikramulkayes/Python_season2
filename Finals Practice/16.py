def func(lst):
    dic = {}
    for elm in lst:
        elm = str(elm)
        year = "20"+elm[0:2]
        subcode = elm[3:5]
        if subcode == "01":
            sub = "CSE"
        elif subcode == "41":
            sub = "CS"
        elif subcode == "21":
            sub = "EEE"
        else:
            sub = "Other"
        if year not in dic.keys():
            dic[year] = {sub:[elm]}
        else:
            if sub not in dic[year].keys():
                dic[year][sub] = [elm]
            else:
                temp = dic[year][sub]
                temp.append(elm)
                dic[year][sub] = temp
    return dic

IDs = ['20201199','21121347','20141052','20341121','21241369','21272199','19241187','19101007','20101035', '21121875', '19141534', '19301552', '21141135', '21365001']
print(func(IDs))
