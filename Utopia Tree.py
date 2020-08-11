n=int(input())
locycle=[]
for i in range(0,n):
    clength=int(input())
    locycle.append(clength)

loflength=[]
for i in locycle:
    loftree=0
    for p in range(0,i+1):
        
        if(p%2==0):
            loftree=loftree+1
        elif(p%2!=0):
            loftree=2*loftree
    loflength.append(loftree)

for i in loflength:
    print(i)
