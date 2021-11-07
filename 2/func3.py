def maxmin(min,max,count):
    sum1 = 0
    for elm in range(min,max,count):
        sum1 += elm
    return sum1
num1 = int(input("Enter a number: "))    
num2 = int(input("Enter anoter number: "))
num3 = int(input("Enter your limit: "))
print(maxmin(num1,num2,num3))
