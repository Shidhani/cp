import math
n = int(input())
a = [0]*1000
f =1
l = list(map(int,input().split()))
# l2 = list(l)

if n <= 2:
    print("YES")
# elif l2 ==l:
    # print("NO")
else:
    for i in l:
        a[i]+=1
    for i in a:
        if i > math.ceil(len(l)/2):
            f = 1 #no
            break
        else:
            f= 0 # yes

    if f ==1:
        print("NO")
    else:
        print("YES")
  