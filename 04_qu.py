# finding area of a triangle 

a=float(input("Enter length of side 1: "))
b=float(input("Enter length of side 2: "))
c=float(input("Enter length of side 3: "))

if((a+b)>c and (b+c)>a and (c+a)>b):
    s=(a+b+c)/2
    area=(s*(s-a)*(s-b)*(s-c))**0.5
    print(area)
else:
    print("Invalid triangle")
