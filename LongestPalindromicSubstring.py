def LongestPalindrome():
    n = len(st)
    maxLen,start=1,0
    for i in range(1,n):
        low=i-1
        high=i
        while(low>=0 and high<n and st[low]==st[high]):
            if high-low+1>maxLen:
                start = low
                maxLen = high-low+1
            low-=1
            high+=1

        low=i-1
        high=i+1
        while(low>=0 and high<n and st[low]==st[high]):
            if high-low+1>maxLen:
                start = low
                maxLen = high-low+1
            low-=1
            high+=1
    return(st[start:start+maxLen])


st = input()
print(LongestPalindrome())


