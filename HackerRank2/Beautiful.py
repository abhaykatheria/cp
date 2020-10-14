def rev(n):
    string1=str(n)
    rev_num=int(string1[::-1])
    return(rev_num)

def divide(s,e,k):
    count=0
    for i in range(s,e+1):
         if (i-rev(i))%k==0:
             count +=1
         else:
             continue
    print(count)
s,e,k=map(int,input().split())
divide(s,e,k)