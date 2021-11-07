def bmi(height,weight):
    height = height /100
    sum1 = weight / (height*height)
    sum1 = round(sum1,1)
    if sum1 < 18.5:
        return(f"Score is {sum1}. You are Underweight")
    elif sum1 >= 18.5 and sum1 <= 24.9:
        return(f"Score is {sum1}. You are Normal")
    elif sum1 >=25 and sum1 < 30:
        return(f"Score is {sum1}. You are Overweight")
    else:
        return(f"Score is {sum1}. You are Obese")

num1 = int(input("Enter your height: "))
num2 = int(input("Enter your weight: "))
print(bmi(num1,num2))
