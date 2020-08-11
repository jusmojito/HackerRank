m=[int(element) for element in input().split()]
#n=int(input())
rangeset=list()
#cond_one=list()
#cond_two=list()
ic_one=list()
ic_two=list()

a=[int(element) for element in input().split()]
b=[int(element) for element in input().split()]

maxa=max(a)
maxb=max(b)
mina=min(a)
minb=min(b)

rangeset.append(maxa)
rangeset.append(maxb)
rangeset.append(mina)
rangeset.append(minb)

#print("Max a:",maxa)
#print("Max b:",maxb)
#print("Min a:",mina)
#print("Min b:",minb)

#print(rangeset)

maxrset=max(rangeset)
minrset=min(rangeset)
#print(maxrset,minrset)

for p in range(1,101):
    cond_one=list()
    for item in a:
        
        if(p%item==0):
            if item not in cond_one:
                cond_one.append(item)
            #print("cond_one",cond_one)
        else:
            continue
    if(len(cond_one)==len(a)):
        ic_one.append(p)
        #print("ic_one",ic_one)
    else:
        continue
    
for t in (ic_one):
    cond_two=list()
    for item1 in b:
        if(item1%t==0):
            cond_two.append(item1)
            #print("cond_two",cond_two)
        else:
            continue
    if(len(cond_two)==len(b)):
        ic_two.append(t)
        #print("ic_two",ic_two)
    else:
        continue

#print("cond_one",cond_one)
#print("ic_one",ic_one)
#print("cond_two",cond_two)
#print("ic_two",ic_two)

sol=len(ic_two)
print(sol)
        
