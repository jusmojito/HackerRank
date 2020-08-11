n=int(input())
matrix=list()
for v in range(0,n):
    row=input().split()
    matrix.append(row)

#print(matrix)    

sumleftd=0
for l in range(0,n):
    #print(matrix[l])
    for li in range(0,n):
        if l==li:
            #print((matrix[li])[li])
            sumleftd+=int((matrix[li])[li])
        
#print(sumleftd)


sumrightd=0

c=n-1
for l in range(0,n):
    #print(matrix[l])
    for li in range(0,n):
        r=l
        if li==c:
            #print((matrix[r])[c])
            sumrightd+=int((matrix[r])[c])
    c=c-1
#print(sumrightd)

ddiff=abs(sumleftd-sumrightd)

print(ddiff)
