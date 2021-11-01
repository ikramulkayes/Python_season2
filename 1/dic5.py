dic = {
    "1": [".",",","?","!",":"],
    "2": ["A","B","C"],
    "3":["D","E","F"],
    "4":["G","H","I"],
    "5":["J","K","L"],
    "6":["M","N","O"],
    "7":["P","Q","R","S"],
    "8":["T","U","V"],
    "9":["W","S","Y","Z"],
    "0":[" "]


}

word = input("Enter your string: ")
final = ""

for elm in word:
    elm = elm.upper()
    for key,val in dic.items():
        if elm in val:
            count = val.index(elm) + 1
            temp = count * key
            final += temp
print(final)