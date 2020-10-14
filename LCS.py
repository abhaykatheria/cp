st1 = input()
st2 = input()
dp = [[0 for i in range(len(st2)+1)] for i in range(len(st1)+1)]
for i in range(1,len(st1)+1):
    for j in range(1,len(st2)+1):
        if st1[i-1]==st2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    
l1,l2 = len(st1),len(st2)
ans =''
while(l1>0 and l2>0):
    if dp[l1-1][l2]==dp[l1][l2-1] and dp[l1][l2]!=dp[l1-1][l2]:
        ans+=st2[l2-1]
        l2-=1
        l1-=1
    elif dp[l1][l2]==dp[l1][l2-1]:
        l2-=1
    elif dp[l1][l2]==dp[l1-1][l2]:
        l1-=1
    else:
        l2-=1

print(ans[-1::-1])
        
            
