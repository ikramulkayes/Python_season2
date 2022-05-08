times = int(input())
lst = []
for i in range(times):
    k = int(input())
    lst.append(k)


for word in lst:

    word = int(word)
    if word >= 1900:
        print("Division 1")
    elif word >= 1600:
        print("Division 2")
    elif word >= 1400:
        print("Division 3")
    else:
        print("Division 4")