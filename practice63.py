def remainder(a,b):
    if a==0 or b ==0:
        if a > b:
            if b ==0:
                return None
            else:
                return a % b
        elif b > a:
            if a ==0:
                return None
            else:
                return b % a
    elif a > b:
        return a%b
    else:
        return b%a
print(remainder(17,5))