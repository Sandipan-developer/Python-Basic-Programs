# checking if a number is armstrong or not

num=int(input("Enter the number:"))
ornum=num
total=0
count=0

# counting number of digits 
while(num!=0):
    num=num//10
    count+=1

num=ornum

# Adding all digits to the power count
while(num!=0):
    d=num%10
    total+=(d**count)
    num//=10


# printing the number is armstrong or not
if(total==ornum):
    print("Armstrong number")

else:
    print("Not an armstrong number")