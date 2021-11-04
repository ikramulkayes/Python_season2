word = "Bracu1234"

lowersorted = []
upersorted = []
digits = []

even = ""
odd = ""
finaldigit = ""
finallower = ""
finalupper = ""
final = ""

for elm in word:
    if elm.isalpha():
        if elm.isupper():
            upersorted.append(elm) #putting lower upper and digits in different variables
        else:
            lowersorted.append(elm)
    elif elm.isdigit():
        digits.append(elm)

lowersorted = sorted(lowersorted) #sorting lower and upper variabel
upersorted = sorted(upersorted)

for elm in digits:
    elm = int(elm)
    if elm % 2 == 0:
        even += str(elm)   #storing even odd in different variable
    else:
        odd += str(elm)
finaldigit =  odd + even

for elm in lowersorted:
    finallower += elm

for elm in upersorted:
    finalupper += elm

final = finallower + finalupper + finaldigit

print(final)
