word1 = input("Enter a word: ")
word2 = input("Enter another word: ")

word1 = word1.lower()
word2 = word2.lower()

dic1 = {}
dic2 = {}

for elm in word1:
    if elm in dic1.keys():
        count = dic1[elm]
        count += 1
        dic1[elm] = count
    else:
        dic1[elm] = 1

for elm in word2:
    if elm in dic2.keys():
        count = dic2[elm]
        count += 1
        dic2[elm] = count
    else:
        dic2[elm] = 1
if dic1 == dic2 and word1 != word2:
    print("Those strings are anagrams.")
else:
    print("Those strings are not anagrams.")

