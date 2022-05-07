word = input()
word = word.split("+")

word = sorted(word)
final = ""
for elm in word:
    final += elm + "+"
final = final.rstrip("+")
print(final)