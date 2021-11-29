def actors(word):
    dic = {}
    fdigit = ""
    middigit = ""
    ldigit = ""
    count = 0
    for elm in word:
        elm = elm.split(" ")
        if elm[0] == "USA":
            fdigit = "1"
        if elm[0] == "UK":
            fdigit = "2"
        if elm[2] == "DanielCraige":
            middigit = "04"
        if elm[2] == "TomCruise":
            middigit = "03"
        if elm[2] == "BradPitt":
            middigit = "02"
        if elm[2] == "EddieRedmayne":
            middigit = "01"
        ldigit = str(count)
        count += 1
        id = fdigit + middigit + ldigit
        id = int(id)
        if elm[0] not in dic.keys():
            dic[elm[0]] = [(elm[1],id)]
        else:
            temp = dic[elm[0]]
            temp.append((elm[1],id))
            dic[elm[0]] = temp
    print(dic)
        
        

my_tuple = ("UK NoTimeToDie DanielCraige", "USA MissionImpossible TomCruise", "USA TopGun TomCruise", "USA Troy BradPitt", "UK Skyfall DanielCraige", "UK TheTheoryOfEveryting EddieRedmayne", "UK FantasticBeast EddieRedmayne", "USA Seven BradPitt")

actors((my_tuple))