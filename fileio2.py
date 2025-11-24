l=[]

n1=int(input("Enter number 1:"))
l.append(n1)

n2=int(input("Enter number 2:"))
l.append(n2)

n3=int(input("Enter number 3:"))
l.append(n3)

n4=int(input("Enter number 4:"))
l.append(n4)

n5=int(input("Enter number 5:"))
l.append(n5)

f=open("list.txt","w")

for item in l:
    f.write(str(item)+"\n")

f.close()