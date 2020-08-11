itemnkar=[int(element) for element in input().split()]
itemn=itemnkar[0]
k=itemnkar[1]

narr=[int(element) for element in input().split()]
itemtotal=narr
b=int(input())


del narr[k]
#print(narr)

sofissp=sum(narr)#sum of items she should pay
msp=sofissp/(2)#money she pays
#print(sofissp)
#print(msp)

if(msp==b):
    print("Bon Appetit")

else:
          print(int(b-msp))
