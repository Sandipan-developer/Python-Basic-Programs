# Printing fibonacci series

a=0
b=1

num=int(input("Enter the number of terms:"))
if(num<=0):
    print("Invalid number of terms")

else:

    if(num==1):
        print(a)

    elif(num==2):
        print(a)
        print(b)

    else:
        print(a)
        print(b)
        for item in range(0,num-2):
            c=a+b
            print(c)
            a=b
            b=c