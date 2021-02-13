n = int(input())
a=0
b=0

for i in range(n):
    s = int(input())
    for i in range(s):
        l = list(map(int, input().split()))
        if(l[0]) == 1:
            a +=1
        elif(l[0]) == 2:
            b+=1
        if (a==b):
            print("YES")
        else:
            print("NO")

