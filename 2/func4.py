def order(choice,location = "Mohakhali"):
    menu = {
        "BBQ Chicken Cheese Burger": 250,
        "Beef Burger": 170,
        "Naga Drums":200
    }
    
    item = menu[choice]


    item += item * 0.08
    if location == "Mohakhali":
        item += 40
    else:
        item += 60
    return item

item = input("ITEM: ")
location = input("Location: ")

if location == "":
    print(order(item))
else:
    print(order(item,location))

    