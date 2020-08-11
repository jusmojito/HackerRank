n=int(input())
l=list()
output=list()
errl=list()
fname=input("Enter name f")
fhandle=open(fname)
for line in fhandle:
    output.append(line.rstrip())
#print(output)

for i in range(0,n):
    inp=[int(element) for element in input().split()]
    ca=inp[0]
    cb=inp[1]
    mc=inp[2]
    if(ca<cb<mc):
        l.append("Cat B")
    elif(cb<ca<mc):
        l.append("Cat A")
    elif(ca<mc<cb):
        if(cb-mc<mc-ca):
            l.append("Cat B")
        elif(cb-mc>mc-ca):
            l.append("Cat A")
        elif(cb-mc==mc-ca):
            l.append("Mouse C")
    elif(ca>cb>mc):
        l.append("Cat B")
    elif(cb>ca>mc):
        l.append("Cat A")
    elif(ca>mc>cb):
        if(ca-mc<mc-cb):
            l.append("Cat A")
        elif(ca-mc>mc-cb):
            l.append("Cat B")
        elif(ca-mc==mc-cb):
            l.append("Mouse C")
    else:
        print(i,ca,cb,mc)
        
#print(l)
#for v in l:
    #print(v)
print("l:",len(l))
print("output:",
      len(output))
for i in range(0,101):
    if(output[i]!=l[i]):
        errl.append(i)
    
