num = int(input("Enter a number: "))
sum = ""
for elm in range(1,num+1):
    sum += f"=== Iteration {elm} ===\n"
    if elm %2==0:
        

        for selm in range(1,elm+1):
            sum += selm *"X" + "\n"
        #sum = sum.rstrip("\n")
    else:
        temp = ""
        for selm in range(1,elm+1):
            temp += str(selm)
        sum += (temp + "\n")*elm
sum = sum.rstrip("\n")
print(sum)

