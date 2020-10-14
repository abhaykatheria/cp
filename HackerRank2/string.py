def repeat(n,string):
    count,total,count2=0,0,0
    string1=string*2**13
    r=n%len(string)
    q=n//len(string)
    for i in range(0,len(string)):
        if string[i]=="a":
            count +=1
    total=count*q
    for k in range(0,r):
        if string[k]=="a":
            count2 +=1
    print(total+count2)

string=str(input())
n=int(input())
repeat(n,string)