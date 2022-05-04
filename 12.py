def mouly(word,num):
    final = []
    for elm in word:
        for selm in word:
            fnum = abs(elm-selm)
            if fnum !=0 and fnum == num:

                templst = [elm,selm]
                if templst[::-1] not in final:
                    final.append([elm,selm])
    if len(final) >0:
        return(final)
    else:
        return f"Not Possible"

print(mouly([1, 5, 9, 13], 5))