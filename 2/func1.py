def frac(num1,num2):
    if num1 == 0 or num2 ==0:
        return 0
    else:
        sum1 = num1 / num2
        sum1 = str(sum1)
        sum1 = sum1.split(".")
        final = "0."+ sum1[1][0]
        final = float(final)
        return final
print(frac(4,1))