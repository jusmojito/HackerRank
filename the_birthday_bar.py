n=int(input())
noc=[int(element) for element in input().split()]
p=[int(element) for element in input().split()]
d=p[0]
m=p[1]
count=0

for i in range(0,len(noc)):
    suma=0
    sumlist=list()
    if(i+m<=len(noc)):
        for j in range(i,i+m):
            #suma=suma+noc[j]
            sumlist.append(noc[j])
            suma=sum(sumlist)
            #print("INLOOP:",suma)
            #print("i :",i)
            #print("j:",j)
            if(suma==d and len(sumlist)==m):
                count+=1
            
if(n==1 and d==noc[0] and m==1):
    count=1
print(count)

#for i in range(0,len(noc)):
 #   print("index:",i,"value:",noc[i])
'''4,7
5,8
10,13
16,19
17,20
20,22
23,25
24,27
25,28
'''
