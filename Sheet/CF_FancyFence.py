
n = int(input())

for i in range(n):
    a = int(input())
    e = 360.0/(180-a)
    absolute = abs(e)
    rounded = round(e)   
    if(e>=3):
        if(abs(absolute - rounded) < 1e-9):
            print("YES")
            print(e)

    else:
        print("NO")
