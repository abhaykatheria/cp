def Search(S):
    l=len(S)
    p=len(S)/3
    count=0
    string=S
    for i in range(0,l):
        if string[i:i+3]=="SOS":
            count +=1
            string=S[i+3:]
        else:
            continue
    return abs(p-count)
S=str(input())
result=Search(S)
print(int(result))
            