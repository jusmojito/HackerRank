n=int(input())
s = input()

up_downc = 0
count=0

for i in s:
    if(i == 'U'):
        up_downc-=1
    else:
        up_downc+=1
    if(up_downc == 0 and i == 'U'):
        count+=1
print(count)
