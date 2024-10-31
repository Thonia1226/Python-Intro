sheep=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
#Write a python code that will determine how many sheeps are present
sheepcount=0 
basket=[]

def sheep1():
    for i in sheep:
        if i==True:
            sheepcount=sheepcount=+1
            basket.append(i)
        else:
            continue
    print(basket.count(i))

sheep1()

