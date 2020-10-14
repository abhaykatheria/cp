def adv(n):
    m=5
    count =0
    count1=0
    for i in range(1,n+1):
        count +=m//2
        count1=count-count1
        m=count1*3
        count1=count
    print(count)

n=int(input())
adv(n)