word = input("Enter a number: ")
word = int(word)
count =10
while True:
    temp = word % 10
    word = word//10
    if temp % 2==0:
        print(temp,end="")
    if word == 0:
        break