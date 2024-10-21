#mr john took a loan of principal 500k for two years at the r8 of 5%
#write a phyton that will calc the simple interest

def MrJohn():
    principal=500000
    time=2
    rate=5
    si=principal*time*rate/100
    print("This is the interest", si)

MrJohn()