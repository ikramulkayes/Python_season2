lst1 = "2 3 6"
lst2 = "3 4 5"

lst1= lst1.split(" ")
lst2 = lst2.split(" ")

sum1 = 0
final = []

for elm in lst1:
    elm = int(elm)
    for elm2 in lst2:
        elm2 = int(elm2)
        sum1 = elm*elm2
        final.append(sum1)
print(final)
