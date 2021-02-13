n = int(input())

arr = [0]*101 # num of cubes in each level
levels = [0]*n # construct new box arangment
l = list(map(int,input().split())) 

for k in l:
    for j in range(k):
        arr[j]+=1

for s in arr:
    if s !=0:
        for d in range(s):
            levels[(len(levels)-1)-d]+=1

# print(arr)

for p in levels:
    print(p, end=" ")
