arr=[1,2,3,4,4,3]
res=[]
for i in arr:
    if i not in res:
        res.append(i)
print(res)