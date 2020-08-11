n=int(input())

for v in range(n,0,-1):
    #print('#',v,'#')
    for p in range(1,n+1):
        #print(p)
        if (p>=v):
            print("#",end=" ")
        else:
            print(" ")
            


        
