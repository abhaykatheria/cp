def histogram(hist):
    stack = list()
    max_area,index = 0,0
    max_top = -1
    while(index<len(hist)):
        if not stack or (hist[stack[-1]]<=hist[index]):
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            area = hist[top]*((index-stack[-1]-1) if stack else index)
            if area>=max_area:
                max_top=top
            max_area = max(area,max_area)
    while stack:
        top = stack.pop()
        area = hist[top]*((index-stack[-1]-1) if stack else index)
        if area>=max_area:
            max_top=top
        max_area = max(area,max_area)
    t_area = 0
    for i in range(max_top,len(hist)):
        if hist[max_top]>hist[i]:
            break
        t_area+=hist[i]
    for i in range(max_top-1,-1,-1):
        if hist[max_top]>hist[i]:
            break
        t_area+=hist[i]
    print(max_top)
    return(t_area*hist[max_top])

hist = [3,1,6,4,5,2]
print(histogram(hist))