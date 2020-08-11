#l1=[int(element) for element in input().split()]
#l2=[int(element) for element in input().split()]
#l3=[int(element) for element in input().split()]
Matrix = [[0 for x in range(3)] for y in range(3)]
DLR=0
U=0
MH=0
D=0
L=0
MV=0
R=0
DRL=0

for i in range(0,3):
    inp=[int(element) for element in input().split()]
    for j in range(0,3):
        Matrix[i][j]=inp[j]
print(Matrix)


for i in range(0,3):
    for j in range(0,3):
        if(i==j):
            DLR=DLR+Matrix[i][j]
for i in range(0,3):
    for j in range(0,3):
        if(i==0):
            U=U+Matrix[i][j]
for i in range(0,3):
    for j in range(0,3):
        if(i==1):
            MH=MH+Matrix[i][j]
for i in range(0,3):
    for j in range(0,3):
        if(i==2):
            D=D+Matrix[i][j]
for i in range(0,3):
    for j in range(0,3):
        if(j==0):
            L=L+Matrix[i][j]
for i in range(0,3):
    for j in range(0,3):
        if(j==1):
            MV=MV+Matrix[i][j]
for i in range(0,3):
    for j in range(0,3):
        if(j==2):
            R=R+Matrix[i][j]
DRL=Matrix[0][2]+Matrix[1][1]+Matrix[2][0]
print("DLR",DLR)
print("U",U)
print("MH",MH)
print("D",D)
print("L",L)
print("MV",MV)
print("R",R)
print("DRL",DRL)


