lst1 = input("First input: ")
lst2 = input("Second input: ")

lst1 = lst1.split()
lst2 = lst2.split()

lst2 = sorted(lst2)
templst = []
count = 0
while count < int(lst1[1]):       #running the loop for k times
    for elm in lst2:
        elm = int(elm)
        if elm <5:             #checking if the player is acceptable
            elm += 1          
            templst.append(elm)
    lst2 = templst.copy()
    templst = []
    count += 1
#print(lst2)
final = len(lst2)//3
print(final)
    
