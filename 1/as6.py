password = "ohmybracu"
lowerflag = True
upperflag = True
digitflag = True
spflag = True
splst = ("_" , "$" , "#", "@")
for elm in password:
    if elm.isalpha():
        if elm.islower():
            lowerflag = False
        elif elm.isupper():
            upperflag = False
    elif elm.isdigit():
        digitflag = False
    elif elm in splst:
        spflag = False
final = ""

if lowerflag:
    final += "Lowercase character missing, "
if upperflag:
    final += "Uppercase character missing, "
if digitflag:
    final += "Digit missing, "
if spflag:
    final += "Special character missing, "

if len(final) == 0:
    print("OK")
else:
    final = final.rstrip(", ")
    print(final)