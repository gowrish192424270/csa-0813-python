a=5
for i in range(a,0,-1):
    for j in range(a-i,0,-1):
        print(" ",end="")
    for k in range(i,0,-1):
        print("*",end=" ")
    print()