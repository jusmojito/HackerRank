n=int(input())
cmax=0
cmin=0

m=[int(element) for element in input().split()]
maxsc=m[0]
minsc=m[0]

for score in m:
    if(score>maxsc):
        maxsc=score
        cmax=cmax+1
    elif(score<minsc):
        minsc=score
        cmin=cmin+1
print(cmax,cmin)
    
