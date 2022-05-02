word = input("Enter a string: ")
word = word.split()
dic = {}
lst = ["?",".",",","!"]
for elm in word:
    elm.strip(" ")
    for k in lst:
        #print(k)
        if k in elm:
            elm.strip(k)
    num = len(elm)
    if num not in dic.keys():
        dic[num] = [elm]
    else:
        temp = dic[num]
        temp.append(elm)
        dic[num] = temp
print(dic)
