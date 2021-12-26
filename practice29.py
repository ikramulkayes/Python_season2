loop = int(input("Enter number: "))
lst = []
for elm in range(loop):
    word = input("Enter the input: ")
    lst.append(word)

dic = {}

for elm in lst:
    elm = elm.split()
    print(elm)
    year = elm[0]
    year = int(year)
    name = elm[2]
    game = elm[1]
    if name not in dic.keys():
        dic[name] = {}
   
        
    elif year in dic[name].keys():
        temp = dic[name][year]
        temp.append(game)
        dic[name][year] = temp
    if year not in dic[name].keys():
        dic[name][year] = [game]


print(dic)