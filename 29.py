times = int(input())
lst = []
sum1 = 0
pluslst = ["++X","X++"]
minuslst = ["--X","X--"]
for elm in range(times):
    k = input()
    lst.append(k)
for elm in lst:
    if elm in pluslst:
        sum1 += 1
    else:
        sum1 -=1
print(sum1)
