#include <bits/stdc++.h>
using namespace std;

# define ll long long
ll mod=pow(10,9)+7;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    ll t,n,x,y,z,w;
    cin>>t;
    while(t--){
        cin>>n;
        int ar[n];
        for(int i=0;i<n;i++)
            cin>>ar[i];
        int flag=1;
        sort(ar,ar+n);
        for(int i=0;i<n-1;i++)
        if(ar[i+1]-ar[i]>1){
            flag=0;
            break;
        }
        if(flag)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
}

