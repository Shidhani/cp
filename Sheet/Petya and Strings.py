
# import string

# alpha = list(string.ascii_lowercase)

# for n in alpha:
#     print(n)
#     print(ord(n))


a = input()
b = input()
a = a.lower()
b = b.lower()
i,j = 0,0
# print(a,b)
for q in range(len(a)):
    if a[q] > b[q]:
        i+= ord(a[q])
        break
    elif a[q] < b[q]:
        j+= ord(b[q])
        break
# for w in range(len(b)):
#     j+= ord(b[w])

if(i==j):
    print(0)    
elif(i>j):
    print(1)

elif(i<j):
    print(-1)
# print(i,j)