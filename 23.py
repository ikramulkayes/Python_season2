name = input()
lst = []
for elm in name:
    if elm not in lst:
        lst.append(elm)
if len(lst) %2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
