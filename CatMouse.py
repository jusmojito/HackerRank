q=int(input())
l=list()


for i in range(0,q):
    inp=[int(element) for element in input().split()]
    ca=inp[0]
    cb=inp[1]
    mc=inp[2]
    if(abs(ca-mc)<abs(cb-mc)):
        l.append("Cat A")
    elif(abs(ca-mc)>abs(cb-mc)):
        l.append("Cat B")
    else:
        l.append("Mouse C")
for v in l:
    print(v)

'''output=list()
errl=list()
fname=input("Enter name f")
fhandle=open(fname)
for line in fhandle:
    output.append(line.rstrip())
    
for i in range(0,100):
    if(output[i]!=l[i]):
        errl.append(i)
print(errl)'''
