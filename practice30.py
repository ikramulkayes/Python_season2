def gp(marks):
    if marks>=90:
        return 4.0
    if marks>=85:
        return 3.7
    if marks>=80:
        return 3.3
    if marks>=75:
        return 3.0
    if marks>=70:
        return 2.7
    if marks>=65:
        return 2.3
    if marks>=60:
        return 2.0
    if marks>=57:
        return 1.7
    if marks>=55:
        return 1.3
    if marks>=52:
        return 1.0
    if marks>=50:
        return 0.7
    return 0.0

dict = {}
while True:
    userInput = input()
    if userInput == "STOP":
        break

    ls = userInput.split(" ")

    GPA = 0
    for i in range(1,len(ls)):
        marks=float(ls[i])  #converting marks to number
        GPA= GPA + gp(marks)*3.0

    GPA = GPA/(3 * (len(ls) - 1))   #calculating GPA

    GPA = round(GPA,2)  #round to 2 decimal places
    dict[ls[0]]=GPA      #adding to dict

print(dict)     #printing dict