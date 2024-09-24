#Write a python code that will take from the list of numbers below move 2 to the end of the list

list=[1,0,2,0,1,6,2,7,5,2]
for item in list:
    if item==2:
        list.remove(item)
        list.append(item)
print(list)


for item in list:
    if item==2:
        list.remove(item)
        list.append(item)
print(list)

listofitems=["banana" , "groundnut" , "apple" , "pawpaw" , "orange"]
for item in listofitems:
    print(item)