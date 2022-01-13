def ascii_string(word):
    dic = {}
    for elm in word:
        sum1 = 0
        count = 0
        for smelm in elm:
            if count %2 != 0:
                sum1 += ord(smelm)
            count += 1
        dic[sum1] = elm
    print(dic)

ascii_string(["apple","orange"])