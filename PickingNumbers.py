n=int(input())
lon=sorted([int(e) for e in input().split()])
l_of_l=[]
l=[]
num=None
print(lon)
for p in range(0,len(lon)-1):
    if(lon[p]!=lon[p+1] or abs(lon[p]-lon[p+1])!=1):
        l.append(lon[p])
    else:
        print(l)
        l_of_l.append(l)
for i in l_of_l:
    print(i)

print(l_of_l)
