a=5
for i in range(0,a):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(0,i):
        print("*",end=" ")
    print()