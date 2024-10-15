# list1 - Write a python code to function list of numbers together
list=[11,21,31,41,51,61]
def functionlist():
    total=1
    for i in list:
        total=total*i
        f=total/50
    print("This is my final result ", f)
functionlist()