a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[4,5,6],[1,2,3],[7,8,9]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(a)):
    for j in range(len(a[0])):
        for k in range (len(b)):
            c[i][j]+=a[i][k]*b[k][j]
print(c)