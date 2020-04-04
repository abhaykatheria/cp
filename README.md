# cp
practise-init

#### basic looping over a map
```
// size - size of array
#include<map>
int MissingNumber(int arr[], int size){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */
    map<int,int> m;
    for(int i=0;i<size;i++)
    {
        m[arr[i]]=m[arr[i]]+1;
    }
    for(std::pair<int,int> element : m )
    {
        if(element.second>1)
            return element.first;
    }

}

```
#### itertools in python to generate combinations

```
## Read input as specified in the question.
## Print output as specified in the question.
import itertools
n= int(input())
arr=[int(x) for x in input().split()]
aa = int(input())
lis =  list(itertools.combinations(arr,3))

for x in lis:
    if sum(x) == aa:
        temp = sorted(x)
        print(str(temp[0])+" "+str(temp[1])+" "+str(temp[2]))
```
#### longest consecutive sequence is a bitch

```
