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
***
### inversion count

basic inversion count can be implemented via bruteforce but that takes order of n2 time we can bring that to nlogn by using the
logic of merge sort basically any test cases which are above 10^5 and have n2 time complexity will 10^10 time usually 10^8  is the
limit allowed by most judges. 
>Some question where we can divide the problem into sub problems can be solved by mergeSort logic maybe.

```
void merge(long long arr[], long long l, long long m, long r,long long * count) 
{ 
    long long i, j, k; 
    long long n1 = m - l + 1; 
    long long n2 =  r - m; 
  
    /* create temp arrays */
    long long L[n1], R[n2]; 
  
    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++) 
        L[i] = arr[l + i]; 
    for (j = 0; j < n2; j++) 
        R[j] = arr[m + 1+ j]; 
  
    /* Merge the temp arrays back into arr[l..r]*/
    i = 0; // Initial index of first subarray 
    j = 0; // Initial index of second subarray 
    k = l; // Initial index of merged subarray 
    while (i < n1 && j < n2) 
    { 
        if (L[i] <= R[j]) 
        { 
            *count+=n1-i;
            arr[k] = L[i]; 
            i++;
        } 
        else
        { 
            arr[k] = R[j]; 
            j++; 
        } 
        k++; 
    } 
  
    /* Copy the remaining elements of L[], if there 
       are any */
    while (i < n1) 
    { 
        arr[k] = L[i]; 
        i++; 
        k++; 
    } 
  
    /* Copy the remaining elements of R[], if there 
       are any */
    while (j < n2) 
    { 
        arr[k] = R[j]; 
        j++; 
        k++; 
    } 
}

void mergeSort(long long arr[], long long l, long long r,long long* count) 
{ 
    if (l < r) 
    { 
        // Same as (l+r)/2, but avoids overflow for 
        // large l and h 
        long long m = l+(r-l)/2; 
  
        // Sort first and second halves 
        mergeSort(arr, l, m,count); 
        mergeSort(arr, m+1, r,count); 
  
        merge(arr, l, m, r,count); 
    } 
} 
long long solve(long long A[], long long n)
{
	// Write your code here.
    long long* count;
    *count=0;
    mergeSort(A,0,n,count);
    cout<<*count;
}
```
***
#### Chef's restaurant using map its not a good solution but it works locally....:P
the input array size was 10^5 larfe so On^2 was out of option so i used maps as they use red black tree in which searching is in
logn so that makes this complexity mlogn.
[https://www.codechef.com/submit/CHEFRES]

```
#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    long n,m;
	    cin>>n>>m;
	    long long arr,dept;
	    map<long long,long long> intervals;
	    for(long i=0;i<n;i++)
	    {
	        cin>>arr>>dept;
	        intervals[arr]=dept;
	    }

	    long long person[m];

	    for(long i=0;i<m;i++)
	    {
	    cin>>person[i];
	    }
	    map<long long , long long>::iterator it,temp;
	    for(long i=0;i<m;i++)
	    {
	       it=intervals.lower_bound(person[i]);
	       temp = it;
           temp--;
	       if(it->first==person[i])
	       {
                std::cout << 0 << std::endl;
	       }
	       if(it->first>person[i])
	       {

	           if(temp->second>person[i] && temp->first<person[i])
	           {
	               std::cout << 0 << std::endl;
	           }
	           else if(it->first-person[i]<128849018849)
	            cout<<it->first-person[i]<<endl;
	           else
	           cout<<-1<<endl;

	       }
	    }

	}
	return 0;
}

```
***
### variation from 2015 [zonal olympiad codechef](https://www.codechef.com/ZCOPRAC/problems/ZCO15002)
This was awsome question it can be solved with 3 different approaches first one is brute force obviously. we can also do the binary search on the sorted array and find the minimum index for which variation>=k nlogn approach. But we can also use **2 pointer approach to get it in linear time but sorting will take nlogn so total complexity will be nlogn only :P.

```
#include <bits/stdc++.h>
#include<iostream>

#include<algorithm>
int main(void) {
	// your code goes here
    long long n,k;
    std::cin>>n>>k;
    long long arr[n];
    for(long long i=0; i<n;i++)
    std::cin>>arr[i];

    std::sort(arr,arr+n);

    long long i,j;
    i=0;
    j=0;
    long long count = 0;
    while(j<n)
    {
        if(i==j)
        j++;
        if(arr[j]-arr[i]>=k)
        {
        count+=n-j;
        i++;
        continue;}
        else j++;

    }

    std::cout << count;


	return 0;



}

```

