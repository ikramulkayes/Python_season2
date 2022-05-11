word = input()
word = word.split()
lweight = int(word[0])
bweight = int(word[1])
sum1 = 0
while True:
    if lweight > bweight:
        break
    else:
        lweight = lweight*3
        bweight = bweight*2
    sum1 += 1
print(sum1)
    