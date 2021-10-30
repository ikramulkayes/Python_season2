word1 = "harry"
word2 = "hermione"

final = ""

for elm in word1:
    if elm in word2:
        final += elm
for elm in word2:
    if elm in word1:
        final += elm
if len(final)>1:
    print(final)
else:
    print("Nothing in common.")