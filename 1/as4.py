word = "The book is not too good! good too say no! good! too good?"
word = word.split()
final = []
flag = False
temp =""
for elm in word:
    if elm == "too":
        flag = True
        final.append(elm)
    elif flag:
        if not elm[-1].isalpha():
            if elm[:-1] == "good":
                final = final[:-1]
                temp = "excellent" + elm[-1]
                final.append(temp)
                flag = False
                
        elif elm == "good":
            final = final[:-1]
            final.append("excellent")
            flag = False
        else:
            final.append(elm)
            flag = False
    else:
        final.append(elm)
result = ""

count = 0
for elm in final:
    if count == len(final) - 1:
        result += elm
    else:
        result += elm + " "
    count += 1
print(result)

