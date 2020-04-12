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
***
## Backtracking
#### nine queens palcing problem


```
#include<bits/stdc++.h>

using namespace std;

int arr[11][11];

bool possible(int n, int row , int col)
{
    //check col
    for(int i=0;i<row;i++)
        if(arr[i][col]==1)
            return false;
    int i,j;
    
    //check left diagonal
    for(i=row-1,j=col-1;i>=0&&j>=0;i--,j--)
        if(arr[i][j]==1)
            return false;
    //check right diagonal
    for(i=row-1,j=col+1;j<n,i>=0;j++,i--)
        if(arr[i][j]==1)
            return false;
	    
    return true;
}

void nqueenHelper(int n , int row)
{
    cout<<row<<endl;
    //cout<<"inside nqueen helper "<<row<<endl;
    if(row==n)
    {
        for(int i=0;i<n;i++)
        {
                for(int j=0;j<n;j++)
                cout<<arr[i][j]<<" ";

        }
         cout<<endl;
         return;
    }

    for(int col=0;col<n;col++)
    {
        if(possible(n,row,col))
        {
            arr[row][col]=1;
            nqueenHelper(n,row+1);
            arr[row][col]=0;
        }
    }
    return;
}

void nqueen(int n)
{
    memset(arr,11*11,sizeof(int));
    nqueenHelper(n,0);
}


int main()
{
    int n;
    cin>>n;
    nqueen(n);
}
```
- place yourself at the starting point
- now we have to explore the entire matrix
- loop through current row
- check if the location is possible
- if yes then move to the row below check all its postion and so on
- if you reach the last row then print the solution otherwise backtrack


#### rat in a maze

```
#include<bits/stdc++.h>

using namespace std;

int arr[20][20];
int sol[20][20];

void rat(int n,int row, int col)
{
    /*
    so we have this recursive function first we check our constraints
    */		
    //cout<<"inside rat "<<row<<" "<<col<<endl;
    if(row>=n || col>=n || arr[row][col]==0 || row<0 || col<0 || sol[row][col]==1)
        return;
    if(row==n-1 && col==n-1)
    {
        sol[row][col]=1;
        for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cout<<sol[i][j]<<" ";
        cout<<endl;
        sol[row][col]=0;
        return;
    }
    sol[row][col]=1;
    rat(n,row-1,col);
    rat(n,row+1,col);
    rat(n,row,col-1);
    rat(n,row,col+1);
    sol[row][col]=0;
    return;
}


int main()
{
    int n;cin>>n;
    memset(arr,20*20,sizeof(int));
    memset(sol,20*20,sizeof(int));
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>arr[i][j];
    rat(n,0,0);

}

```

#### sudoku solver

```
    #include<bits/stdc++.h>
    #include<math.h>
    using namespace std;
    int arr[9][9];


    bool possible(int x , int row , int col)
    {
        //check row
        for(int i=0;i<=8;i++)
            if(arr[row][i]==x)
                return false;
        //check col
        for(int i=0;i<=8;i++)
            if(arr[i][col]==x)
                return false;
        //check box
        int t,u;

        t=row-(row%3);
        u=col-(col%3);
        for(int i=t;i<=t+3;i++)
            for(int j=u;j<=u+3;j++)
                if(arr[i][col]==x)
                return false;
        return true;

    }
    std::pair<int,int> findEmpty()
    {
        pair<int,int> p;
        for(int i=0;i<=8;i++)
            for(int j=0;j<=8;j++)
                if(arr[i][j]==0)
                    {p.first=i;p.second=j;return p;}
        p.first=-1;
        p.second=-1;
        return p;
    }
    bool solveSudoku()
    {
        pair<int,int> p;
        p=findEmpty();
        if(p.first==-1)
            return true;
        else{
            for(int i=1;i<=9;i++)
                if(possible(i,p.first,p.second))
            {
                arr[p.first][p.second]=i;
                if(solveSudoku())
                {
                    return true;
                }
                else
                    arr[p.first][p.second]=0;
            }

        }
        return false;

    }


    int main()
    {
        char temp[9][9];
        for(int i=0;i<=8;i++)
        cin>>temp[i];
        for(int i=0;i<=8;i++)
            for(int j=0;j<=8;j++)
            arr[i][j]=int(temp[i][j])-48;

        bool t = solveSudoku();

        for(int i=0;i<=8;i++)
            {
                for(int j=0;j<=8;j++)
                cout<<arr[i][j];
                cout<<endl;
                }
    }
```

***
## bit manipulation
-
```
int turnOnIthBit(int n, int i){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */
    
	int a = 1<<i;
    return n|a;
}
```
-
```
int turnOffIthBit(int n, int i){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */
    int a = ~(1<<i);
    return n&a;
}
```
-

```
#include<bits/stdc++.h>
int returnFirstSetBit(int n){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */
    if(n==0)
        return 0;
    int pos = ffs(n);
    return 1<<pos-1;
    
}
```

- 

```
#include<bits/stdc++.h>
int turnOffFirstSetBit(int n){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */
    
    if(n==0)
        return 0;
    int pos = ffs(n);
    int a = 1<<pos-1;
    return n&~a;
}

```
-

```
int clearAllBits(int n, int i){
    /* Don't write main().
     * Don't read input, it is passed as function argument.
     * Return output and don't print it.
     * Taking input and printing output is handled automatically.
     */
	//create mask
    if(n==0)
        return 0;
    int a = 1<<i; // mask making
    a=a-1;
    return a&n;

}
```

***

# awesome sudoku code
```


bool isEmpty(int board[][9],int &row, int &col)
{
    for(int i=0;i<=8;i++)
            for(int j=0;j<=8;j++)
                if(board[i][j]==0)
                {
                    row=i;
                    col=j;
                    return true;
                }
    return false;
}
bool possible(int board[][9],int x ,int row, int col)
{
    //check the row
    for(int i=0;i<=8;i++)
        if(board[row][i]==x)
            return false;
    //check the column
    for(int i=0;i<=8;i++)
        if(board[i][col]==x)
            return false;
    //check the box
    int t= row - (row%3);
    int u=col-(col%3);
    for(int i=t;i<t+3;i++)
            for(int j=u;j<u+3;j++)
                if(board[i][col]==x)
                    return false;
    
	return true;
}
void printSudoku(int board[][9])
{
    for(int i=0;i<=8;i++)
    {
            for(int j=0;j<=8;j++)
			cout<<board[i][j]<<" ";
        cout<<endl;
    }
    cout<<endl;
}
bool sudokuSolver(int board[][9]){

  /* Don't write main().
   *  Don't read input, it is passed as function argument.
   *  Don't print output and return output as specified in the question
  */
	int row,col;
    if(!isEmpty(board,row,col))
    {

        return true;
    }
    else{
    
        for(int i=1;i<10;i++)
    {
        if(possible(board,i,row,col))
        {
            board[row][col]=i;
            if(sudokuSolver(board))
            {
                return true;
            }
            board[row][col]=0;
        }
    }
    return false;
}
    
}
```
***
## Adhoc problems

### codeforces (Equalize)[https://codeforces.com/problemset/problem/1037/C] adhoc awesome problem 
learnt alot from this problem

```
#include<bits/stdc++.h>

using namespace std;

int main(){

    long long  n;cin>>n;
    char a[n],b[n];

    for(int i=0;i<n;i++)
    cin>>a[i];

    for(int i=0;i<n;i++)
    cin>>b[i];

    long cost=0;

    for(int i=0;i<n;i++)
    {
        if(a[i]==b[i])
            continue;
        if(a[i]!=a[i+1]&& a[i+1]!=b[i+1])
        {swap(a[i],a[i+1]);cost++;}
        else{
            if(a[i]=='0')
                a[i]='1';
            else
                a[i]='0';
            cost++;
        }
    }
    cout<<cost;
}
```
### light up the bulbs
in this problem we have to find the min cost again we just found the groups of continuous zro grouped them together and fliped the last one. The approach was not to waste time in actually looping througha rray and getting substrings. that is also needed sometime but not everywhere.

```

#include<bits/stdc++.h>
using namespace std;
int main()
{
    
    long long n,x,y;cin>>n>>x>>y;
    char arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    
    long long groups = 0;
    if(arr[0]=='0')groups++;
    for(int i=0;i<n-1;i++)
    {
        if(( arr[i]=='1' && arr[i+1]=='0' ) )
    		groups++;
    }
    if(groups>0)
    {long long cost = ((groups-1)*min(x,y) )+ y;
     cout<<cost;}
    else if (groups == 0  && arr[0]=='0')
        cout<<y;
    else
        cout<<0;
    
    
	return 0;
}
```

### interesting sequence
the problem was to make all the no. same of given array through some operation keeping the cost minimum. Since constraints were low so brute force was available
we looped through aal the no.s that can be possible soln and checked the cost of converting all the no.s to that then printed it out
>> cost=k*(dec) + l*(inc-dec);
```
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n,k,l;cin>>n>>k>>l;
    
    int arr[n];
    
    for(int i=0;i<n;i++)
        cin>>arr[i];
    
    sort(arr,arr+n);
    
    int min=arr[0];
    int max=arr[n-1];
    long long cost;
    long long  ans =1000000;
    for(int i=min;i<=max;i++)
    {
        cost=0;
        long  long dec=0;
        long long inc=0;
        for(int j=0;j<n;j++)
        {
            if(arr[j]>i)
                dec+=(arr[j]-i);
            else{
                inc+=(i-arr[j]);
            }
            cost=k*(dec) + l*(inc-dec);
        }
       if(cost==0)
           ans=0;
        
       else if(cost<ans && cost>0)
            ans=cost;
	}
	cout<<ans;
}
```

### winning strategy
make array of 123 to n to the given array in minimum no. of swaping ops guven some condn on swapping 
in this we did have to work on the array but we approached the question in reverse manner converting given array to 12345

```
#include<bits/stdc++.h>
using namespace std;
int main() {

	// Write your code here
    long n;cin>>n;
    long arr[n];
    for(int i=0;i<n;i++)
        cin>>arr[i];
    long ts=0;
    for(int i=n-1;i>=0;i--)
    {
        if(arr[i]==i+1)
        {
            continue;
        }
        if(arr[i-1]==i+1)
        {
            swap(arr[i-1],arr[i]);
            ts++;
            continue;
        }
        if(arr[i-2]==i+1)
        {
            arr[i-2]=arr[i-1];
            arr[i-1]=arr[i];
            arr[i]=i+1;
            ts++;ts++;
            continue;
        }
        else
        {
            cout<<"NO";
            return 0;
        }
    }
    cout<<"YES"<<endl<<ts;
        
        
    
}
```


