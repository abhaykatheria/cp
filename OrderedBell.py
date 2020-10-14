n = int(input())
ans = 0
mod = 10**9+7
def ncr(n, r, p): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  
            p - 2, p)) % p 
def calculate(n,i,ans):
    if n==0:
        return 1
    else:
        ans+=(ncr(n,i,mod)*calculate(n-i,i+1,ans))
        return(ans)

print(calculate(n,1,ans))
