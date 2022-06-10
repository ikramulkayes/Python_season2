times = int(input())
lst = []
for elm in range(times):
    m = input()
    k = input()
    lst.append(k)

for elm in lst:
    elm = elm.split()
    numbers = [ int(x) for x in elm ]
    
    count = 0
    templst = []
    while count <len(numbers):
        m = numbers[count]
        for i in range(count+1,len(numbers)):
            #print(i,m)
            templst.append(abs(numbers[i]-m))
        count += 1
    print(min(templst))



