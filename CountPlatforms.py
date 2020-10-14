for _ in range(int(input())):
    n = int(input())
    arrival = list(map(int, input().split()))
    depart = list(map(int, input().split()))
    pair = [(arrival[i], 'a') for i in range(n)] + [(depart[i], 'd') for i in range(n)]
    pair.sort()
    platform = 0
    maxm = 0
    for ch in pair:
        if ch[1]=='a':
            platform+=1
            maxm = max(maxm,platform)
        else:
            platform-=1
    print(maxm)
