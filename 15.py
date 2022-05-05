def function_name(word1,word2):
    dsum = 0
    word1 = word1.split("/")
    word2 = word2.split("/")
    dsum += int(word2[0])-int(word1[0])

    dsum += (int(word2[1])-int(word1[1]))*20

    dsum += (int(word2[2])-int(word1[2]))*20*12
    dsum += 1
    return dsum
print(function_name("3/8/2018", "10/8/2020"))
