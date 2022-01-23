lst = []
dic = {}
loop = int(input("Enter the loop: "))
for elm in range(loop):
    k = input("Enter the numplate: ")
    lst.append(k)
vehicle_chart = {'KA': 'Private Car', 'KHA': 'Private Car', 'GA': 'PrivateCar', 'GHA':'Jeep', 'CH':'Microbus','CHA':'Laguna','JA':'Minibus','JHA':'Bigbus','TA':'Big truck','THA':'Pick-up','DO':'MediumTruck','NO':'Pick-up','PO':'Taxi-cab','VO':'PrivateCar', 'MO':'Pick-up','DA':'CNG','TH':'CNG', 'HA':'Motorbike','LA':'Motorbike','E':'Truck','ZO':'PMOffice Vehicles'}
for elm in lst:
    elm = elm.split()
    bangla = elm[2].strip("-")
    num = elm[3]
    car = vehicle_chart[bangla]
    if car not in dic.keys():
        dic[car] = [1,[num]]
    else:
        temp = dic[car]
        count = temp[0] + 1
        temp[1].append(num)
        temp[0] = count
        dic[car] = temp
print(dic)
