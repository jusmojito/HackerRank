bnm=input().split()
b=bnm[0]
n=bnm[1]
m=bnm[2]
amounts=None
nv=input().split()
mv=input().split()

for vn in nv:
    for vm in mv:
        if (amounts is None):
            amounts=int(vn)+int(vm)
            if(amounts>int(b)):
                amounts=-1
            #print("amounts1",amounts)
        elif(amounts<=int(b)):
            temps=int(vn)+int(vm)
           #print("temps",temps)
            if(temps>amounts and temps<=int(b)):
                amounts=temps
                #print("amounts2",amounts)
print(amounts)

