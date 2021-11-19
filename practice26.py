word = input("Enter a list: ")
word = word[1:-1]
word = word.split(",")
dic = {}
#print(word)
for elm in word:
    elm = elm[1:-1]
    course = elm[:3]
    num = elm[3:]
    num = int(num)
    if course not in dic.keys():
        dic[course] = {}
    if num < 500:
        if "Undergraduate" not in dic[course].keys():
            dic[course]["Undergraduate"] = [elm]
        else:
            temp = dic[course]["Undergraduate"]
            temp.append(elm)
            dic[course]["Undergraduate"] = temp
    if num > 499:
        if "Graduate" not in dic[course].keys():
            dic[course]["Graduate"] = [elm]
        else:
            temp = dic[course]["Graduate"]
            temp.append(elm)
            dic[course]["Graduate"] = temp
print(dic)
