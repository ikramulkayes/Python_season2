num = int(input())
if num %5 == 0:
    final = num//5
elif num % 4==0:
    final = num//4
elif num %3==0:
    final = num//3
elif num%2 ==0:
    final = num //2
else:
    final = num

print(final)