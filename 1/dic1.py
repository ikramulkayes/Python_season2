word1 = "a: 100, b: 100, c: 200, d: 300"
word2 = "a: 300, b: 200, d: 400, e: 200"

word1 = word1.split(", ")
word2 = word2.split(", ")

dic1 = {}
dic2 = {}

for elm in word1:
    elm = elm.split(": ")
    dic1[elm[0]] = int(elm[1])
#print(dic1)

for elm in word2:
    elm = elm.split(": ")
    dic2[elm[0]] = int(elm[1])
#print(dic2)

finallst = []


for key, val in dic2.items():
    if key in dic1.keys():
        temp = dic1[key] + val
        dic1[key] = temp
        if temp not in finallst:
            finallst.append(temp)
    else:
        dic1[key] = val
        if val not in finallst:
            finallst.append(val)
print(dic1)
finallst = sorted(finallst)
finallst = tuple(finallst)
print("Values:",finallst)
