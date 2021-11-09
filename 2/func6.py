def vowelfinder(word):
    vlst = ["a","e","i","o","u"]
    vstring = ""
    word = word.lower()
    count = 0
    for elm in word:
        if elm in vlst:
            vstring += elm + ", "
            count += 1
    
    if vstring == "":
        return "No vowels in the name"
    else:
        vstring = vstring.rstrip(", ")
        return f"Vowels: {vstring}. Total number of vowels: {count}"

word = input("Enter a string: ")
print(vowelfinder(word))
