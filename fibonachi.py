a=9
n=a
next=0
st=0
en=1
while n>0:
    print(st)
    next=st+en
    st=en
    en=next
    n-=1