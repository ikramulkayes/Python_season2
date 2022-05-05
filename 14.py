given_dict = { 'Mike' : ['CSE110','ENG101','MAT110'],              
              'Simon' : ['CSE111','PHY111','MAT110', 'CSE230'],
              'Shawn' : ['CSE110','ENG101','MAT120','CSE230'],
              'Alice' : ['CSE110','ENG091','MAT092']  }


def function_name(given_dict):
    lst = []
    while True:
        k = input("Enter a number: ")
        if k != "STOP":
            lst.append(k)
        else:
            break
    templst = []
    for elm in lst:
        for key,val in given_dict.items():
            if elm in val:
                templst.append(key)
        print(templst)
        templst = []
function_name(given_dict)
