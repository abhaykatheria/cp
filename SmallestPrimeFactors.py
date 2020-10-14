#Smallest Prime Factors and Prime Factors
from collections import defaultdict
spf = defaultdict(int)
def seive():
    for i in range(1,10**6+1):
        spf[i]=i
    for i in range(2,10**6+1,2):
        spf[i]=2
    for i in range(3,10**3+1):
        if spf[i]==i:
            for j in range(i*i,10**6+1,i):
                if spf[j]==j:
                    spf[j]=i

def primeFactors(n):
    factors,factors_freq=set(),defaultdict(int)
    while n!=1:
        factors.add(spf[n])
        factors_freq[spf[n]]+=1
        n=n//spf[n]
    return factors,factors_freq
seive()
print(spf[1000])
print(primeFactors(420))