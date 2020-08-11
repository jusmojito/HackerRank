n=int(input())
c=[int(element) for element in input().split()]
count=0
socksdata=dict()
uniq=list()

for i in range(0,len(c)):
    if(c[i] not in socksdata):
        socksdata[c[i]]=1
        uniq.append(c[i])
    else:
        socksdata[c[i]]+=1

print((socksdata))
print(uniq)
for j in uniq:
    if(int(socksdata[j]/2)!=0):
        count=int(socksdata[j]/2) + count

print(int(count))
        
