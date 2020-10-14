def funnyString(string):
    rev_string=string[::-1]
    l=len(string)
    for i in range(1,l):
        if abs(ord(string[i])-ord(string[i-1]))==abs(ord(rev_string[i])-ord(rev_string[i-1])):
            flag=1
        else:
            flag=0
            break
    if flag==1:
        print("Funny")
    else:
        print("Not Funny")

n=int(input())
for k in range(0,n):
    string=str(input())
    funnyString(string)