lst = []
while True:

    num = input("Enter a number: ")
    if num == "STOP":
        break
    num = int(num)
    lst.append(num)
final = ""
count = 0
checkedlst = []
for elm in lst:
    if elm in checkedlst:
        continue
    else:
        checkedlst.append(elm)
        for elm2 in lst:
            if elm == elm2:
                count += 1
        final += str(elm) + " "+ "-"+" "+ str(count) +" times\n"
        count = 0
final = final.rstrip("\n")
print(final)
