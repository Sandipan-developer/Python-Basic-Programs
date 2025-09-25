# finding prime numbers in an interval
num1=int(input("Enter lower limit:"))
num2=int(input("Enter upper limit:"))

for j in range(num1,num2+1):
    if(j==2 or j==3):
        print(f'{j}')

    else:
        for i in range(2,j):
            if(j%i==0):
                break

        else:
            print(f'{j}')