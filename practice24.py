seq = input("Enter the seq: ")
word = input("Enter the word: ")
dic = {}

for elm in seq: 
    if elm not in dic.keys():
        dic[elm] = 1
    else:
        temp = dic[elm]
        temp += 1
        dic[elm] = temp
lst = []
for key,val in dic.items():
    if key in word:
        lst.append(val)
flst = sorted(lst)
print(f"Number of times {word} can be written: {flst[0]}")