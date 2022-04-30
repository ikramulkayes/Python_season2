a = input("Enter a number: ")
prev = None
flag = True
if len(a)==1:
    flag = False
for elm in a:
    if prev == None:
        
        prev = int(elm)
    else:
        if prev > int(elm):
            prev = int(elm)
        else:
            flag = False
            break
print(flag)