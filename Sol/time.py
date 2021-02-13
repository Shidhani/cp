s = int(input())
for i in range(s):
    l = list(map(int, input().split()))
    f =l[0]
    s =  l[1]
    f2 = abs(f)
    s2 = abs(s)
    if s2==f2:
        r= 1
        if s ==f:
            r =0
    elif s2 > f2:
        r = s2 - f2
        if s>=0 and f<=0:
            r+=1 
        elif s<=0 and f<=0:
            r+=2 
        elif s<=0 and f>=0:
            r+=1

    elif s2 < f2:
        if s<=0 and f<=0:    
            r = f2 - s2
         
        if s>=0 and f>=0:    
            r = f2 - s2
            r+=2

        if s>=0 and f<=0:    
            r = f2 + s2
   
        if s<=0 and f>=0:    
            r = f2 - s2
            r+=1

    print(r)