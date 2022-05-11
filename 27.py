times = int(input())
lst = []
sum = 0
for elm in range(times):
    k = input()
    lst.append(k)
for elm in lst:
    elm = elm.split()
    if elm.count("1")>1:
        sum += 1
print(sum)
