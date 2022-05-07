xsum = 0
ysum = 0
word = input("Enter your directions: ")
for elm in word:
    if elm == "L":
        xsum -= 1
    elif elm == "R":
        xsum += 1
    elif elm == "D":
        ysum -=1
    else:
        ysum += 1
print(f"({xsum},{ysum})")