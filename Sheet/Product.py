
while True:
    try:
        n = int(input())
        m = int(input())
        print(n*m)
    except EOFError:
        break