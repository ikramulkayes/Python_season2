word = input("Enter your ip adresses: ")
val = word[0]
val = int(val)
word = word[1:]
word = word.strip()
word = word.split(",")
dic = {}
for elm in word:
    lst = elm.split(".")

    smallword = lst[:val]
    smallword = ' '.join([str(elem) for elem in smallword]) 
    bigword = smallword + ".0"*(4-val)
    if bigword not in dic.keys():
        dic[bigword] = [elm]
    else:
        temp = dic[bigword]
        temp.append(elm)
        dic[bigword] = temp
print(dic)
    