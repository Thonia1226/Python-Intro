#The length of a rectangle is 42m and the breath is 34m write a python code that will calculate the perimeter
#And also calculate the area
#Then add the perimeter and area together and print out the final results

def rectangle():
    l=42
    b=34
    p=(l+b)*2

    al=42
    bl=34
    a=al*bl

    print("This is the perimeter of the rectangle", p)
    print("This is the area of the rectangle", a)
    d=p+a
    print(d)

rectangle()