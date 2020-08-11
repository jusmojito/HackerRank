c=1

inp=input().split()
x1=int(inp[0])
v1=int(inp[1])
x2=int(inp[2])
v2=int(inp[3])
#print("Input to ho gya")
pos_x1=x1
pos_x2=x2
      
if(((x2>x1) and (v2>v1)) or ((x1>x2) and (v1>v2))):
    print("NO")

else:
    while c!=0:
        pos_x1=pos_x1+v1
        pos_x2=pos_x2+v2

        if(pos_x1!=pos_x2):
            c=c+1
            if(((pos_x2>pos_x1) and (v2>=v1)) or ((pos_x1>pos_x2) and (v1>=v2))):
                print("NO")
                c=0
                
            
        else:
            c=0
            print("YES")
