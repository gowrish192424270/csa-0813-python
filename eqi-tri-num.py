a=7
for i in range(1,a):
    for j in range(0,a-i):
        print(" ",end="")
    for k in range(1,i):
        print(k,end="")
    for k in range(i,0,-1):
        print(k,end="")
    print()
