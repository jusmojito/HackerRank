import bisect

def climbingLeaderboard(scores,alice):
    
    alice=scoresa
    scores=sorted(scores)
    l=len(scores)
    

    
    for p in alice:
        
        ind=bisect.bisect(scores,p)
        
##        print("scores:",scores)
##        print("alice:",alice)
##        print("p",p)
        print(l+1-ind)

n=int(input())

scores=[int(e) for e in input().split()]

setofscores=set(scores)
uniquescores=sorted(list(setofscores),reverse=True)

m=int(input())

scoresa=[int(e) for e in input().split()]

climbingLeaderboard(uniquescores,scoresa)

##can actually use bisect.insort(scores,p) to insert p in scores
##list where list would be  sorted

