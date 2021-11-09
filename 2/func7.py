def palindromechecker(word):
    vanilaword = ""
    for elm in word:
        if elm != " ":
            vanilaword += elm
    
    revword = vanilaword[::-1]
    if vanilaword == revword:
        return "Palindrome"
    else:
        return "Not a palindrome"

word = input("Enter a string: ")
print(palindromechecker(word))