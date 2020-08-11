n=int(input())
s=input()
lists=list(s)
ivalue=dict()
count=0
ioz=list()
ans=0
temp=0
diff=0


'''if(s[0]=="D"):
    count=-1
    ivalue[0]=count
    
elif(s[0]=="U"):
    count=1
    ivalue[0]=count
    '''

for i in range(0,n):
    if(s[i]=="D"):
        count=count-1
        ivalue[i]=count
    elif(s[i]=="U"):
        count=count+1
        ivalue[i]=count
#print(ivalue)

'''for v in ivalue:
    if(ivalue[v]==0):
        try:
            if(ivalue[v-2]==-2):
                ans=ans+1
        except:
            temp=temp+1
print(ans)
'''

for v in range(0,n):
    try:
       # print(ivalue[v])
        if(ivalue[v+2]<=0):
            if((ivalue[v+2]-ivalue[v])==2 and (ivalue[v]-ivalue[v-2])):
                ans=ans+1
                print(v)
    except:
        temp=temp+1
print(ans)
