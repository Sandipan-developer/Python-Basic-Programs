# display multiplication table
num=int(input("Enter the number for which you want multiplication table:"))

for i in range(1,11):
    print(f'{num} x {i} = {num*i}')