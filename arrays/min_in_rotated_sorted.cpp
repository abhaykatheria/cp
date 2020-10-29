#include<bits/stdc++.h>
using namespace std;

int go_bin(int a[],int low,int high) {
    if(high == low) return a[low];

    int mid = (low + high) / 2;

    if(mid < high && a[mid+1] < a[mid]) 
        return a[mid+1];
    if(mid > low && a[mid-1] > a[mid])
        return a[mid];

    if(a[high] > a[mid])
        return go_bin(a,low,mid-1);
    return go_bin(a,mid+1,high);
}

int main() {
    int t,n;
    cin>>t;
    while(t--) {
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++) cin>>a[i];
        cout<<go_bin(a,0,n-1)<<"\n";
    }
}