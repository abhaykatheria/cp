for _ in range(int(input())):
    n = int(input())
    t = int((n*3)/4)
    ans = (t)*'9'+'8'*(n-t)
    print(int(ans))