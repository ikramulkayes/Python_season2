word = input("")
count = 0
w1 = None
w2 = None
for elm in word:
    count += 1
flag = True
if count%2==0:
    flag = True
else:
    flag = False
if flag:
    w1 = word[:(count//2)]
    w2 = word[(count//2):]
else:
    w1 = word[:((count//2)-1)]
    w2 = word[((count//2)+1):]

sum1 = 0
sum2 = 0
for elm in w1:
    elm = int(elm)
    sum1 += elm
for elm in w2:
    elm = int(elm)
    sum2 += elm
if sum1 == sum2:
    print("You won")
else:
    print("You lost")