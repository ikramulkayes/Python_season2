def domainchanger(email,newdom,olddom = "1"):
    email = email.split("@")

    if newdom != email[1]:
        newemail = email[0] + "@"+ newdom
        return f"Changed: {newemail}"
    else:
        newemail = email[0] + "@"+ email[1]
        return f"Unchanged: {newemail}"

email = input("Enter your email: ")
newdom = input("Enter your newdomain: ")
olddom = input("Enter your old domain: ")

if olddom == "":
    print(domainchanger(email,newdom))
else:
    print(domainchanger(email,newdom,olddom))

