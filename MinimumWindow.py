from collections import Counter, defaultdict 
  
def min_window(str, pattern): 
      
    rdict, count = defaultdict(list), Counter(pattern) 
    rpos, res = [], ""  
      
    # Loop only over c exist in pattern 
    for i, c in filter(lambda x: x[1] in pattern, enumerate(str)):  
        if len(rdict) == count:  
  
            # If reached limit, remove 
            rpos.remove(rdict.pop(0)) 
              
        # Add to dict 
        rdict[i].append(i) 
  
        # Add to list 
        rpos.append(i)  
          
        if (len(rpos) == len(pattern) and
           (res =="" or rpos[-1]-rpos[0]<len(res))): 
            res = str[rpos[0]:rpos[-1]+1]  
              
    return res 
  
# Driver Code 
string = "geeksforgeeks"
pattern = "gks"
print(min_window(string, pattern)) 