from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))
rem = defaultdict(int)
rem[0],som=1,0
for i in range(n):
    som+=arr[i]
    rem[som%n]+=1
ans = 0
for key,values in rem.items():
    if values>1:
        ans+=(values*(values-1))//2
print(ans)