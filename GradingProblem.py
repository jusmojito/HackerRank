n=int(input())
gradel=list()
ngl=list()
ng=None
for p in range(0,n):
    grade=input()
    gradel.append(grade)
    #print(gradel)
for g in gradel:
    if(int(g)<38):
        ng=g
        ngl.append(ng)
    elif(int(g)%5==0):
        ng=g
        ngl.append(ng)
    elif(int(g)%5!=0):
        d=int(int(g)/5 +1)
        d=d*5
        c=0
        c=d-int(g)
        if(c<3):
            ng=str(d)
            ngl.append(ng)
        elif(c==3):
            ng=g
            ngl.append(ng)
        else:
            ng=g
            ngl.append(ng)
for newgrades in ngl:
    print(newgrades)
