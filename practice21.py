dna = input("Enter your DNA SEQ: ")
length = int(input("Enter the length of seq: "))

dic = {}
count = 0
while True:
    if (count+length)<= len(dna):
        word = dna[count:(count+length)]
        if word not in dic.keys():
            dic[word] = 1
        else:
            temp = dic[word]
            temp += 1
            dic[word] = temp
        count += 1
    else:
        break
print(dic)
count = 0
maxseq = None
maxnum = None

for key,val in dic.items():
    if maxnum == None:
        maxseq = key
        maxnum = val
    elif val > maxnum:
        maxseq = key
        maxnum = val
for key, val in dic.items():
    if maxnum == val:
        count += 1
if count == 1:
    print(f"Dominant Pattern: {maxseq}")
else:
    print("No Dominant Pattern found.")