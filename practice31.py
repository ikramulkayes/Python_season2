num = input("Enter a number: ")
num = int(num)
sum = ""

sum += "#"*num + "\n"
if num > 3:
    for i in range(num-2):
        sum += "&"*((num-2)//2) + "##"+"&"*((num-2)//2) + "\n"
sum += "#"*num + "\n"
print(sum)
