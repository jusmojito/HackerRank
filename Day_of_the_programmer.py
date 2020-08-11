year=(input())
yeari=int(year)
val=yeari%4
if yeari<1918:
    if(val==0):
       # print("1leap")
        print("12.09."+year)
    elif((val)!=0):
       # print("2notleap")
        print("13.09."+year)
elif (yeari)>1918:
    if(val==0):
        if((yeari%100==0) and (yeari%400!=0)):
           # print("3not leap")
           print("13.09."+year)
        else:
            print("12.09."+year)
           # print("4leap")
    else:
        print("13.09."+year)
else:
    print("26.09."+year)
    

         
