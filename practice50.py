word = input("Enter your word: ")
vowels = ["a","e","i","o","u"]
svowels = []
for elm in word:
    if elm in vowels:
        svowels.append(elm)
print(f"Vowels in input: {svowels}")
print(f"Before swap: {word}")
svowels = svowels[::-1]
fword = ""
count = 0
for elm in word:
    if elm in vowels:
        fword+= svowels[count]
        count += 1
    else:
        fword += elm
print(f"After swap: {fword}")

