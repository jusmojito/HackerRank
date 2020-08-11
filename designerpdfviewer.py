alphasize=[int(e) for e in input().split()]
al="abcdefghijklmnopqrstuvwxyz"
alpha=list(al)
d={}
for i,j in zip(al,alphasize):
    d[i]=j
##print(d)
word=input()
##print(word)
ulword=list(set(word))
##print(ulword)
maxh=0
for p in ulword:
    if(d[p]>maxh):
        maxh=d[p]

l=len(word)
##print(l)
area=l*maxh
print(area)
