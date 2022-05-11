times = int(input())
lst = []
for i in range(times):
    k = input()
    lst.append(k)
a = 1
b = 1
finallst = []
for elm in lst:
    elm = elm.split()
    print(elm)
    x = int(elm[0])
    y = int(elm[1])
    a = 1
    b = 1
    flag = True
    while True:
        if b < y/1.5 and flag:
            if y % (x*b) ==0:
                sum1 = x*b
                a= 1
                while sum1 != y and sum1 < y and a < y/2:
                    a+= 1
                    sum1 = x*(b**a)
                    if sum1 == y:
                        break
                    print(a)
                    k = b**a
                   # print(k)
                   # print("Sum")
                   # print(sum1)
                if sum1 == y:

                    flag = False
        elif b > y/1.5:
            a= 0
            b = 0
            flag = False
            break
        elif flag == False:
            break


        b+= 1
        #print(b)
        #print(flag)
        #print(y)
    finallst.append((a,b))
for elm in finallst:
    print(f"{elm[0]} {elm[1]}")
    