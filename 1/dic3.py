lst = input("Enter your dictionary: ")
lst = lst.split(", ")
dic = {}

for elm in lst:
    elm = elm.split(" : ")
    if elm[1] in dic.keys():
        temp = dic[elm[1]]
        temp.append(elm[0])
        dic[elm[1]] = temp
    else:
        dic[elm[1]] = [elm[0]]
print(dic)
