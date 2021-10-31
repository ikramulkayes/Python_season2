lst = []
while True:

    num = input("Enter a number: ")
    if num == "STOP":
        break
    num = int(num)
    lst.append(num)
dic = {}

for elm in lst:
    if elm in dic.keys():
        count = dic[elm]
        count += 1
        dic[elm] = count
    else:
        dic[elm] = 1

for key,value in dic.items():
    print(str(key)+" - "+str(value)+" times")
