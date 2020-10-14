#include<bits/stdc++.h>
using namespace std;

// BIT

// store sum of range y(inclusive) to x(exclusive)
// getSum() log(n)
// update() log(n)

// given an array store that in BIT such that getSum and update operation done in log(n) time
// in getSum() parent of x can be get from operation  x - (x & (-x))
// in update() parent of x can be get from operation  x + (x & (-x))


// this method can also be used to find inversions in an array


int *BITree;
int N;

int getSum(int index) {
    int sum = 0;
    index += 1;
    while(index > 0) {
        sum += BITree[index];
        index -= ( index & (-index) ); 
    }
    return sum;
}

void update(int index, int val) {
    index += 1;
    while(index < N) {
        BITree[index] += val;
        index += ( index & (-index) );
    }
}

void create_BITree(int n,int a[]) {
    N = n;
    BITree = new int[N];
    memset(BITree,0,sizeof(BITree));
    for(int i=0;i<n;i++) {
        update(i,a[i]);
    }
}

void BIT(int n,int a[]) {
    N = n;
    BITree = new int[N];
}



int main() {
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++) cin>>a[i];
    create_BITree(n,a);
    for(int i=0;i<n;i++) cout<<a[i]<<" \n"[i == n-1];
    cout<<getSum(5)<<"\n";
    // a[2] += 3; 
    // update(2,3);
    // for(int i=0;i<n;i++) cout<<a[i]<<" \n"[i == n-1];
    // cout<<getSum(5)<<"\n";

    // to count inversion
    int b[n];
    for(int i=0;i<n;i++) b[i] = a[i];
    sort(b,b+n);
    for(int i=0;i<n;i++) {
        a[i] = lower_bound(b,b+n,a[i]) - b + 1;
    }
    for(int i=0;i<n;i++) cout<<a[i]<<" ";
    BIT(n,a);
}