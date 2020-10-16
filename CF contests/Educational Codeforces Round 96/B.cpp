#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll mod=1e9 + 7;

int32_t main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ll t,n,x,y,z,k;
    cin>>t;
    while(t--){
        cin>>n>>k;

        ll ar[n];
        for(ll i=0;i<n;i++)
            cin>>ar[i];
        sort(ar,ar+n);

        ll mx=0;
        for(int i=n-1;i>=0 && k>=0;i--,k--){
            mx+=ar[i];
        }

        cout<<mx<<endl;

    }

}