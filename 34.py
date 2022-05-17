times = int(input())
lst = []
for elm in range(times):
    k = input()
    lst.append(k)
flag = True
for elm in lst:
    elm = elm.split()
    a = int(elm[0])
    b = int(elm[1])
    c = int(elm[2])
    x = int(elm[3]) -a
    y = int(elm[4]) - b
    if x ==0 and y ==0:
        print("YES")
    elif x <= 0 and y >0:

            y = y- c
            if y <= 0:
                #print("1")
                print("YES")

            else:
                #print("2")
                print("NO")
    elif y <=0 and x >0:
            x = x- c
            if x <= 0:
                #print("3")
                print("YES")
            else:
                #print("4")
                print("NO") 
    elif x >0 and y >0:
        x = x - c
        if x >0:
            #print("5")
            print("NO")
        elif x <0:
            y = y +x
            if y <=0:
                #print("6")
                print("YES")
            else:
                #print("7")
                print("NO")
        else:
            #print("8")  
            print("NO")
    else:
        print("YES")



    

