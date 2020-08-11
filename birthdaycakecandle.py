def birthdayCakeCandles(x,y):
        age=x
        hocarr=y
        p=max(hocarr)
        count=0
        for o in hocarr:
                if o==p:
                        count=count+1
                else:
                        continue
        print(count)

age=int(input())
hoc=input().split()
hocarr = [int(mem) for mem in hoc]
birthdayCakeCandles(age,hocarr)
