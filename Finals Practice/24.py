def take_order():
    lst = []
    price_list={'Juice':30, 'Fried Rice':150, 'Burger':50, 'Pizza':110, 'Fried Chicken':90, 'Noodles':70}
    while True:
        word = input("Enter your order: ")
        if word == "X":
            break
        else:
            lst.append(word)
    sum1 = 0
    for elm in lst:
        sum1 += price_list[elm]
    return sum1

sum1 = 0
for elm in range(3):
    k = take_order()
    print(f"Total cost: {k}")
    sum1 += k
print(f"Total income of the day: {sum1}")

