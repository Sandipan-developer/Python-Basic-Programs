# find the largest number among 3 numbers
a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
c=int(input("Enter number 3:"))

if(a>b and a>c):
    print(f'{a} is greatest')

elif(b>a and b>c):
    print(f'{b} is greatest')

else:
    print(f'{c} is greatest')