word = "coDaaa123AIng"
final = ""
flag = False
for elm in word:
    if flag:
        if elm.isupper():
            break
            
        final += elm
    if elm.isupper():
        flag = True
if final == "":
    print("BLANK")
else:
    print(final)