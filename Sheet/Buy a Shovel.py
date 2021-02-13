l = list(map(int,input().split()))
p = l[0]
c = l[1]
flag = False
n=1
while not flag:
    f = n*p
    if f%10 ==0:
        r=n
        flag= True
    elif (f-c) % 10 == 0:
        r = n
        flag = True
    else:
        n+=1

if flag:
    print(r)