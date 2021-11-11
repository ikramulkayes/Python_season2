def stringfixer(sentence):
    sentence = sentence.split()
    symbollst = [".","!","?"]
    flag = False
    count = 0
    final  = ""
    for elm in sentence:
        if count ==0:
            elm = elm.capitalize()
            count += 1
        if flag:
            elm = elm.capitalize()
            flag = False
        for letter in elm:
            if letter in symbollst:
                flag = True
        if elm == "i":
            elm = elm.capitalize()
        elif "i" in elm:
            if len(elm) == 2:
                if elm[1] in symbollst:
                    elm = elm.capitalize()
        final += elm + " "
    final = final.rstrip()
    return final

sentence = input("Enter your string: ")
print(stringfixer(sentence))            
        
