n=[]
p=[]

for i in range (0,10):
    u=int(input())
    if u==-1:
        break
    if u<0:
        n.append(u)
    elif u>0:
        p.append(u)
if len(n)>0:
    print("avg of negative nums is ",sum(n)/len(n))
else:
    print("no negative nums")
if len(p)>0:
    print("avg of positive nums is ",sum(p)/len(p))
else:
    print("no positive nums")