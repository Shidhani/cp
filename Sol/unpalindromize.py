n = int(input())

for i in range(n):
    s = int(input())
    l = list(map(int,input().split()))
    lSorted = list(l)
    lSorted.sort()
    minl = lSorted[0]
    maxl = lSorted[-1]
    d = maxl - minl

    
    l1 = l[0:l.index(maxl)+1]
    if l[-1] != maxl:
      l2 = l[l.index(maxl)+1:] 
    else:
        l2 = [-10]
    # print(l1)
    # print(l2)

    i,j,k =0,len(l2)-1,0
    l1_n,l1_m,l2_n,l2_m = 0,0,0,0

    while l1[i]==l1[0]:
        l1_n+=1
        i+=1
    while l2[j]==l1[0]:
        l2_n+=1
        j-=1

    while l2[k]==l1[-1]:
        l2_m+=1
        k+=1
    # print( l1_n,l2_n,l2_m)
    
    if l2[-1] > 0:
      r = l1_n*len(l2)
    else:
        r = l1_n
    # p = l2_n*l2_m
    if l2_n !=0 and l2_m!=0:
        r+=((len(l1)- l1_n)*l2_n )+(l2_m-1)
    print(r)