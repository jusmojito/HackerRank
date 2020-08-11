st_string = input().split(' ')
st_in_int = [int(num) for num in st_string]

ab = input().split(' ')
ab_in_int = [int(num) for num in ab]

mn_str = input().split(' ')
mn_int = [int(num) for num in mn_str]

apple_str = input().split(' ')
apple_int = [int(num) for num in apple_str]

orange_str = input().split(' ')
orange_int = [int(num) for num in orange_str]

m_house = 0
for mem in apple_int:
    if(st_in_int[1]>=(ab_in_int[0]+mem)>=st_in_int[0]):
        m_house = m_house + 1

n_house = 0
for mem in orange_int:
    if(st_in_int[0]<=(ab_in_int[1]+mem)<=st_in_int[1]):
        n_house = n_house + 1

print(m_house)
print(n_house)
