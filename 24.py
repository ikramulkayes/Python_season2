word = input()
word = int(word)
count = 2
scount = 2
flag = True
while flag:
    while True:
        sum = count + scount
        if sum == word:
            flag = False
        elif sum > word:
            break
        scount += 2
    count += 2
    if (count)> word:
        break
if flag:
    print("NO")
else:
    print("YES")


