dic = {}
while True:
    word = input("Enter your grades: ")
    if word == "STOP":
        break
    word = word.split()
    lst = []
    for elm in word[1:]:
        elm = int(elm)
        lst.append(elm)
    dic[word[0]] = lst

fdic = {}
sum1 = 0
grade = 0
#print(dic)
for key,val in dic.items():
    sum1 = 0
    length = len(val)
    #print(length)
    for elm in val:
        if elm >= 90:
            grade = 4
        elif elm >= 85 and elm < 90:
            grade = 3.7
        elif elm >= 80 and elm < 85:
            grade = 3.3
        elif elm < 80 and elm >= 75:
            grade = 3.0
        elif elm < 75 and elm >= 70:
            grade = 2.7
        elif elm < 70 and elm >= 65:
            grade = 2.3
        elif elm < 65 and elm >= 60:
            grade = 2.0
        elif elm <60 and elm >=57:
            grade = 1.7
        elif elm <57 and elm >=55:
            grade = 1.3
        elif elm <55 and elm >= 52:
            grade = 1.0
        elif elm < 52 and elm >=50:
            grade = 0.7
        else:
            grade = 0
        sum1 += grade * 3
    sum1 = sum1 / (length*3.0)
    sum1 = round(sum1,2)
    fdic[key] = sum1
print(fdic)

