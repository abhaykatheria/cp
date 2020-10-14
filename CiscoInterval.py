n = int(input())
arr = []
for _ in range(n):
    name,inTime,outTime = map(str,input().split(","))
    hr,mi,sec = map(int,inTime.split(":"))
    itime = hr*60*60 + mi*60 + sec
    hr,mi,sec = map(int,outTime.split(":"))
    otime = hr*60*60 + mi*60 + sec
    arr.append((itime,otime,name))
arr.sort()
maxm = arr[-1][1]
count = [0]*(maxm+2)
for itime,otime,name in arr:
    count[itime]+=1
    count[otime]-=1

for i in range(1,maxm+2):
    count[i]+=count[i-1]

for queries in range(int(input())):
    time = input()
    hr,mi,sec = map(int,time.split(":"))
    time = hr*60*60 + mi*60 + sec
    print(count[time])