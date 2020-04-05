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

***
#### aggresive cows
```
#include<bits/stdc++.h>
using namespace std;

bool check(int d,int arr[],int n,int c)
{
    //shit is wrong in this function
    //this function works well
    c--;
    int curr = arr[0];
    //put the first cow at 1st slot;
    //then loop through remaining
    for(int i=1;i<n;i++)
    {
        //if the distance b/w the slot under inspection and the last occupied slot ie curr is greater then d 
        //then put the cow there update curr and decrease the counter of cow
        //but what if the first distance that is allowed here is greater than d or all the other distance are greater than d
        //then in that case our answer is not d but the minimum distance found her naaa....
        if(arr[i]-curr>=d)
        {
            curr=arr[i];
            c--;
        }
    }
    if(c==0)
        return true;
    else 
        return false;
}

int main()
{
    // t = no. of test cases
    int t;
    cin>>t;
    while(t--)
    {
        int n,c;
        // n is size of array of slots available
        // c is no. of cows
        cin>>n>>c;
        int arr[n];
        for(int i=0;i<n;i++)
        cin>>arr[i];
        // sorting the slots arra
        sort(arr,arr+n);
        //implementing sort of binary search
        //we know the maximum distance b/w 2 cows would be 1st slot - last slot 
        // minimum distance would be zero all the cows in same slot
        //and we have to find the maximum minimum distance b/w 2 cows
        //so what i can do is loop through each possible minimum distance and check if that works out or not but that will
        //not work cause then we will have on2 time complexity.
        //here what i will do is that i will apply the approach of binary search.
        //we have to find the maximum minimum distance for which slotting is possible.
        
        //what i meant by slotting is possible that suppose i've [1,2,4,8,9] and c=3 and d=3
        //so i will place my first cow at 1 then second at 4 third at 8.8-4>3 so here my min distance is 3
        
        //but suppose d=4 then its not possible because first we will put at 1 then at 8 8-1>4 but we will run out spaces for other cows
        //so any case above d=3 is useless
        //thus we can apply binary search logic here
         
        start=0;
        last=arr[n-1]-arr[0];// this is the maximum distance 
        d=0;
        while(start<=last)
        {
            mid = start + (last-start)/2;
            //we have to check given distance is working or not 
            //rest is self explanatory
            if(check(mid,arr,n,c));
            {
                if(d>mid)
                    d=mid;
                start=mid+1;
            }
            else{
                last = mid-1;
            }
        }
        
    }
}

```
