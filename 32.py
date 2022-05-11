word = input()
word = word.split()
sum1 = 0
for elm in range(1,int(word[2])+1):
    sum1 += elm*(int(word[0]))
if int(word[1])<sum1:
    final = sum1 - int(word[1])
else:
    final = 0
print(final)