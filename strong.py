import math
a=145
c=0
n=a
while a>0:
    b=a%10
    c+=math.factorial(b)
    a//=10
if n==c:
    print("strong")
else:
    print("not")

