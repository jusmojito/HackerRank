def climbingLeaderboard(scores,alice):
    
    alice=scoresa
    

    
    for p in alice:
        scores=uniquescores
        scores.append(p)
        ind=(sorted(scores,reverse=True)).index(p)+1
        
##        print("scores:",scores)
##        print("alice:",alice)
        print(ind)
        scores.remove(p)

n=int(input())

scores=[int(e) for e in input().split()]

setofscores=set(scores)
uniquescores=sorted(list(setofscores),reverse=True)

m=int(input())

scoresa=[int(e) for e in input().split()]

climbingLeaderboard(uniquescores,scoresa)

