def inPlaceRemoval(string):
    st=list(string)
    check = [False]*256
    curr_index,rep_index=0,0
    while(curr_index<len(st)):
        if check[ord(st[curr_index])]==False:
            check[ord(st[curr_index])] = True
            st[rep_index]=st[curr_index]
            rep_index+=1
        curr_index+=1
    return("".join(st[:rep_index]))



for _ in range(int(input())):
    st = input()
    check = [False]*256
    ans =''
    for i in range(len(st)):
        if check[ord(st[i])]==False:
            check[ord(st[i])] = True
            ans+=st[i]
    print(inPlaceRemoval(st))   
