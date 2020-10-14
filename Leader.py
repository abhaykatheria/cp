for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    temp = [arr[-1]]
    #%%
    for i in range(n-2,-1,-1):
        if temp[-1]<=arr[i]:
            temp.append(arr[i])
    for i in range(len(temp)-1,-1,-1):
        print(temp[i],end= ' ')
    print()