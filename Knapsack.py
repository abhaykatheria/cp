def knapsack(dp,curr_index,capacity,size,value):
    if curr_index == 0 or capacity ==0:
        return (0)
    if dp[curr_index][capacity]!=-1:
        return (dp[curr_index][capacity])
    elif  size[curr_index-1] > capacity:
        dp[curr_index][capacity]=knapsack(dp,curr_index-1,capacity,size,value)
    else:
        dp[curr_index][capacity] = max(value[curr_index-1] + knapsack(dp,curr_index-1,capacity-size[curr_index-1],size,value),knapsack(dp,curr_index-1,capacity,size,value))

    return(dp[curr_index][capacity])



n,W = map(int,input().split())
size = list(map(int,input().split()))
value = list(map(int,input().split()))
dp = [[-1 for i in range(W+1)] for j in range(n+1)]
print(knapsack(dp,n,W,size,value))