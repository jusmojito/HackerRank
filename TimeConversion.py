s=input().split(':')

hour=s[0]
minute=s[1]
secM=s[2]

seconds=secM[:2]
meridian=secM[2:]

if (meridian=='PM') and (hour!='12'):
    hour=int(hour)
    hour=hour+12
    hour=str(hour)
elif (meridian=='AM') and (hour=='12'):
    hour='00'

time=(hour)+':'+(minute)+':'+(seconds)
print(time)
