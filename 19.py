word = input("Enter your message: ")
count = 0
final = ""
for elm in word:
    count = 0
    if elm != " ":
        for selm in word:
            if elm == selm:
                count += 1
        num = ord(elm) + count
        elm = chr(num)
        final += elm
    else:
        final += " "
print(final)
