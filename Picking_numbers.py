n=int(input())
sn=[int(element) for element in input().split()]
sn.sort()
same=list()
print(sn)
for i in range(0,n-1):
    if(sn[i]==sn[i+1]):
        for v in same:
            if(sn[i]-v==1):
                same.append(sn[i])
                same.append(sn[i+1])
    elif(sn[i+1]-sn[i]==1):
        same.append
print(same)
