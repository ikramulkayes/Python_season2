def func(word):
    word = word.split(", ")
    dic = {"Magic":[],"Normal":[]}
    for elm in word:
        decide = ""
        
        first = elm[0]
        first = int(first)
        sum1 = 0
        for sval in elm[1::]:
            sum1 += int(sval)
        if first == sum1:
            decide = "Magic"
        else:
            decide = "Normal"
        dic[decide].append(int(elm))
    fdic = {}
    for key,val in dic.items():
        fdic[key] = tuple(val)
    return fdic

word = input("Enter your numbers: ")
print(func(word))
        
        
        
