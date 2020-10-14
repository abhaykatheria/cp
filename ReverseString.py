for _ in range((int(input()))):
    s = input()
    arr = s.split('.')
    arr = arr[-1::-1]
    ans = '.'.join(str(i) for i in arr)
    print(ans)