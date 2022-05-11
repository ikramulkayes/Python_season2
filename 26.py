times = int(input())
finallst = []
for i in range(times):
    k = int(input())
    templst = input()
    templst = templst.split()
    count = 1
    for elm in templst:
        if templst.count(elm) == 1:
            finallst.append(count)
        count+= 1
for elm in finallst:
    print(elm)
