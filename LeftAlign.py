def align(n,text):
    ans,curr,l = [],"",0
    for ch in text.split():
        if len(ch)>n:
            return "CAN NOT BE ALGIN"
    i=0
    while(i<len(text)):
        t = i+n
        if t<len(text)-1:
            if text[t+1]==" ":
                ans.append(text[i:t+1])
            else:
                while text[t]!=" ":
                    t-=1
                ans.append(text[i:t])
        else:
            ans.append(text[i:])
        i=t+1
    st = "\n".join(ans)
    return(st)

n = int(input())
st = input()
print(align(n,st))