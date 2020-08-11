n=int(input())
lon=input().split() #list of numbers
pos=0.0
neg=0.0
zeroes=0.0

for v in range(0,n):
    nwe=int(lon[v])
    #print(nwe)
    
    if nwe<0:
        neg+=1.0
    elif nwe>0:
        pos+=1.0
    else:
        zeroes+=1.0
print(pos/n)
print(neg/n)
print(zeroes/n)
