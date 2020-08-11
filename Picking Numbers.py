n=int(input())
i=[int(e) for e in input().split()]
##print(i)

i=sorted(i)
##print(i)
c=1
d={}

setofi=set(i)
uniquelist=sorted(list(setofi))
##print(uniquelist)

maxsingle=0
    
for p in uniquelist:
    d[p]=i.count(p)
    if(maxsingle<d[p]):
        maxsingle=d[p]
##print("maxsingle",maxsingle)
##print(d)

if(len(uniquelist)==1):
    print(maxsingle)

elif(len(uniquelist)>1):
         
    res = list(zip(uniquelist, uniquelist[1:] + uniquelist[:1])) 
##    print(res)
    c={}
    maxa=0
    for e in res:
        if((e[1]-e[0])<2):
            c[e[0]]=d[e[0]]+d[e[1]]
            
            if(maxa<c[e[0]]):
                maxa=c[e[0]]
        
    if(maxsingle>maxa):
        print(maxsingle)
    else:
        print(maxa)
        

