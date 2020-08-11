t=int(input())
for p in range(0,t):

    n,k=[int(e) for e in input().split()]

    atime=sorted([int(e) for e in input().split()])

    dos={} #dictionary of timearrival

    count=0
    for i in atime:
        if(i not in dos and i<=0):
            dos[i]=atime.count(i)
            count=count+dos[i]

    if(count>=k):
        print("NO")
    else:
        print("YES")





