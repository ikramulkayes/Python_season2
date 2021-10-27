word = "ApplE"
upcount = 0
locount = 0
for elm in word:
    if elm.isupper():
        upcount += 1
    elif elm.islower():
        locount+= 1
if upcount > locount:
    print(word.upper())
else:
    print(word.lower())