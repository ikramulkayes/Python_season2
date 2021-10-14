
#lst = list("one","two","three")
lst = ["one","two","three"]
lst = ["Ronaldo","Messi","Rivaldo","Hazard"]
val = min(lst[::2]+["Ronaldhinho"])
print(val)



lst = [2,4,6,8,10,12,14,16]
lst.reverse()
print(lst)
lst = [2,4,6,8,10,12,14,16]
lst = lst[-1:-(len(lst)+1):-1]
print(lst)
lst = [2,4,6,8,10,12,14,16]
lstk = lst[::1][7::-1]
print("JAJA")
print(lstk)
lst = [2,4,6,8,10,12,14,16]
lst = lst[7:0:-1]
print(lst)



lst = [2,4,6,8,10]
lst_comp = [sum(lst[0:i+1]) for i in range(0,len(lst))]
print(lst_comp)