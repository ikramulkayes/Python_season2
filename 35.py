times = int(input())
lst = []
for elm in range(times):
    k = input()
    lst.append(k)
for elm in lst:
    prev = ""
    for selm in elm:
        if prev == "":
            prev = selm
        elif prev == "?" or prev == "1":
            if elm == "0":
                print("1")

            