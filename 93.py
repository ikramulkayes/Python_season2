word = input("Enter a number: ")
dic = {}
bigdaddy = ""
bigdaddylen = 0
for elm in range(len(word)+1):
  
        #print("first",elm)
        
        for elm2 in range(elm+1,len(word)+1):
            #print("second",elm2)
            k = word[elm:elm2]
            m1 = k[0:len(k)//2]
            m2 = k[len(k)//2::]
            if len(m1) == len(m2):
                flag = True
                if m1 == m2:
                    flag = False
                for gg in m1:
                    if gg != m1[0]:
                        flag = False
                for gg in m2:
                    if gg != m2[0]:
                        flag = False
                if flag:
                    temp = word.count(k)
                    dic[k] = temp
                    if len(k) > bigdaddylen:
                        bigdaddy = k
                        bigdaddylen = len(bigdaddy)

for k,v in dic.items():
    print(f"{k} - {v} times")
print(f"Longest Pattern - {bigdaddy}")
            

    
