f=open("rand.txt","r")

# data=f.readline()

# while(data!=""):
#     print(data)
#     data=f.readline()

for item in f:
    print(item)

f.close()
