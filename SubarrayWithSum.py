for _ in range(int(input())):
    n,target_sum = map(int, input().split())
    arr = list(map(int, input().split()))
    prefix = {}
    curr_sum,flg = 0,0
    for i in range(n):
        curr_sum += arr[i]
        if curr_sum == target_sum:
            print(1,i+1)
            flg=1
            break
        if curr_sum - target_sum in prefix:
            print(prefix[curr_sum - target_sum]+2,i+1)
            flg=1
            break
        prefix[curr_sum] = i
    if flg==0:
        print(-1)


