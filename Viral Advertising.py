n=int(input())

shared=5
cumulative=0
liked=int(shared/2)
cumulative=liked+cumulative

for i in range(0,n-1):
    shared=liked*3
    liked=int(shared/2)
    cumulative=cumulative+liked

print(cumulative)
