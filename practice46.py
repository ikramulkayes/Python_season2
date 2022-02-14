def opditector(word):
    word = word.split(" ")
    print(word)
    dic = {}
    for elm in range(0,len(word),2):
        print(elm)
        name = word[elm]
        num = word[elm+1]
        
        dic[name] = num
    fdic = {}
    op = ""
    for k,v in dic.items():
        i = v[0:3]
        if i =="017" or i == "013":
            op = "Grameenphone"
        elif i == "018":
            op = "Robi"
        elif i == "016":
            op = "Airtel"
        else:
            op = "Others"
        if op not in fdic.keys():
            fdic[op] = {k:v}
        else:
            fdic[op][k] = v
    final = {}

    return fdic

print(opditector("Bob 01632342392 Alice 01346734123 Britney 01803544535 Aeron 01723454642 Smith 01923457890 Tarek 01866392233"))


    

