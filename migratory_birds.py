n=int(input())
ar=[int(element) for element in input().split()]

mbirds=dict()

for i in range(0,len(ar)):
    if ar[i] not in mbirds:
        mbirds[ar[i]]=1

    else:
        mbirds[ar[i]]+=1
#print(mbirds)

maxbirds= None
keyn=-1
for key in mbirds:
    if maxbirds is None:
        maxbirds=mbirds[key]
    else:
        if(mbirds[key]>maxbirds):
            maxbirds=mbirds[key]
            keyn=key
        elif(mbirds[key]==maxbirds):
            if key<keyn:
                keyn=key
            else:
                continue
            
print(keyn)


'''
for i in range(0,len(ar)):
                if(mbirds[key]==ar[i]):
                    mbirdskey=i
                elif(maxbirds==ar[i]):
                    maxbirdskey=i
            if(mbirdskey<maxbirdskey):
                keyn=key
            elif(maxbirdskey<mbirdskey):
                keyn=maxbirds
'''
