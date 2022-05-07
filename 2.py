word = input("")
word = word[1:-1]
word = word.split(", ")
lst = []
for elm in word:
    
    num = int(elm)
    sum = 0
    product = 1
    for selm in elm:
        sum += int(selm)
        product = product*int(selm)
    lst.append([num,sum,product])
print(lst)