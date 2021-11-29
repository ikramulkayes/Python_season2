def ipdef(word):
    num = word[0]
    num = int(num)
    word = word[1::]
    word = word.strip()
    word = word.split(",")
    dic = {}
    for elm in word:
        val = elm
        elm = elm.split(".")
        felm = elm[0:num]
        fword = ""
        for i in felm:
            fword += i + "."
        fword = fword.rstrip(".")
        fword = fword + ".0"*(4-num)
        
        if fword not in dic.keys():
            dic[fword] = [val]
        else:
            temp = dic[fword]
            temp.append(val)
            dic[fword] = temp
    return dic

print(ipdef("2 192.168.30.10,168.192.100.30,192.168.55.10,240.169.10.10,168.192.43.90,192.169.100.45"))

