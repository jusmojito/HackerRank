n = int(input())
m = int(input())

x1 = int(m/2)
if(m==n-1 and n%2==0):
    x2=1
else:
    x2 = int((n-m)/2)

if(x1>x2):
    print(x2)
elif(x2>x1):
    print(x1)
else:
    print(x1)
