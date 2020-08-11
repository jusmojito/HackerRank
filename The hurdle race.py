n,k =  [int(e) for e in input().split()]

a=[int(e) for e in input().split()]

if(max(a)>k):
    d=max(a)-k
else:
    d=0

print(d)
