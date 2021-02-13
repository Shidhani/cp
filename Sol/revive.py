n = int(input())

for i in range(n):
    l = list(map(int, input().split()))
    r=0
    u = l[1]
    x =l[2]
    m =[]
    for i in range(u):
        d= list(map(int, input().split()))
        d.pop(0)
        
        # print(d)
    b =[]
    v= list(map(int, input().split()))
    for k in d:
        b.append(l[k])
        b.sort(reverse= True)
        m.append(b)
    print(m)
    # for j in m:
    #     for i in range(x):
    #         while j[i] != None:
    #             r+=j[i]

print(r)

