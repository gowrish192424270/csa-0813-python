# a=6858
# b=int(str(a)[::-1])
# print(b)
# print(type(b))

a=int(23903)
b=0
while a>0:
    d=a%10
    b=b*10+d
    a=a//10
print(b)