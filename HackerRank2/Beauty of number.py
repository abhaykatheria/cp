def beauty_of_number(n):
    beauty=(n//1)^1
    for i in range(2,n+1):
        beauty ^=(n//i)^i
    print(beauty)
    
t=int(input())
for q in range(0,t):
    n=int(input())
    beauty_of_number(n)
        
        
    