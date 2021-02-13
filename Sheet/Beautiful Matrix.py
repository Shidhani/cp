i=0
j=0
r=[]
c = 0
for l in range(5):
    r = list(map(int,input().split()))
    if 1 in r :
        i= l
        j = r.index(1)

while i < 2:
    i+=1
    c+=1
while i > 2:
    i-=1
    c+=1
while j < 2:
    j+=1
    c+=1
while j > 2:
    j-=1
    c+=1

print(c)
# print(i,j)