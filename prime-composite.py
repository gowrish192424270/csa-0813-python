a=[23,4,2,8,43,3]
c,b=0,0
for i in a:
    isprime=True
    for j in range(2,i):
        if i%j==0:
            isprime=False
            break
    if isprime:
        c+=1
    else:
        b+=1

print("prime nums are",c)
        
print("composite nums are",b)