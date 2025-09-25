# check a number is prime or not
num=int(input("Enter numbers greater than or equal to 2:"))

if(num==2 or num==3):
    print(f'{num} is prime')

else:
    for i in range(2,num):
        if(num%i==0):
            print(f'{num} is non-prime')
            break

    else:
        print(f'{num} is prime')