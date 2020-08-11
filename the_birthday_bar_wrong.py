n=int(input())
noc=[int(element) for element in input().split()]
p=[int(element) for element in input().split()]
d=p[0]
m=p[1]
count=0
for i in range(0,5):
    for j in range(i+1,5):
        sum=noc[i]+noc[j]
        if(sum==d):
            count+=1
            
print(count)
        
