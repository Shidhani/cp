
n = int(input())

c = list(map(int,input().split()))
c.sort(reverse=True)
a = []
# print(c)
for i in range(len(c)):
    if(sum(a)<= sum(c)):
        # print(sum(a), sum(c))
        g = c.pop(0)
        a.append(g)
        # print(a,c)

print(len(a))