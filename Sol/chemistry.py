

n = int(input())
s = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    e = 0
    for i in range(s-1):
        l.pop(0)
        e+= sum(l)

    print(e % 100)

