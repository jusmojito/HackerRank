p=[int(element) for element in input().split()]
n=p[0]
k=p[1]
int_arr=[int(element) for element in input().split()]
count=0

for i in range(0,len(int_arr)):
    for j in range(i+1,len(int_arr)):
        if(i<j):
            sumpair=int_arr[i]+int_arr[j]
            if(sumpair%k==0):
                count=count+1
        else:
            continue

print(count)
        
