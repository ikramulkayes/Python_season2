lst = []
loop = int(input("Number of advertisements: "))
for elm in range(loop):
    temp = input("Enter your advertisement: ")
    temp = temp.split()
    lst.append(temp)
dic = {}
for elm in lst:
    key = elm[4]
    if key not in dic.keys():
        dic[key] = {elm[1][2::]+elm[2]+elm[3]:[elm[0],elm[-1]]}
    else:
        dic[key][elm[1][2::]+elm[2]+elm[3]] = [elm[0],elm[-1]]
print(dic)
