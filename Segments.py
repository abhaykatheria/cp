segment = [[2,6],[1,4],[8,12]]

def maximalSegment(segment):
    segment.sort()
    minm = 10**18
    newSegment = []
    for sub in segment:
        newSegment.append((sub[0],sub[1]))
    segment = newSegment
    for sub in segment:
        minm = min(minm,sub[1]-sub[0])
    l,r=0.0,1.0*minm
    while(l<r):
        mid = (l+r)/2
        lst = []
        for p1,p2 in segment:
            lst.append([p1,p2])
        flag = 1
        lst[0][1] = lst[0][0]+mid
        for i in range(1, len(segment)):
            if lst[i][0] < lst[i-1][1]:
                lst[i][0] = lst[i-1][1] 
            if lst[i][1] - lst[i][0]<mid:
                flag=0
                break
            else:
                lst[i][1] = lst[i][0]+mid
        if flag:
            l=mid
        else:
            r = mid-0.0000001
    return (l)

print(maximalSegment(segment))