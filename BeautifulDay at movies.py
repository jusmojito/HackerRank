r1,r2,k=[int(e) for e in input().split()]
c=0
for i in range(r1,r2+1):
    s=str(i)
    diff=int(s)-int((s)[::-1])
    if(diff%k==0):
        c=c+1

print(c)

