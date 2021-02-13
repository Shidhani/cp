r = 0
n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    if (sum(l)>=2):
        r += 1

print(r)