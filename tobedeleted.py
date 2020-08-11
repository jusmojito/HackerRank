num = int(input())

str_arr = input().split()
num_arr = [int(mem) for mem in str_arr]

day_mon = input().split()
dm = [int(mem) for mem in day_mon]

count = 0
length = len(num_arr)
while(length>=1):
    lst = num_arr[length-dm[1]:length]
    #print(lst)
    total = 0
    for i in lst:
        total = total + i
        #print(total)
    if(total == dm[0]):
        count+=1
    length-=1
print(count)
