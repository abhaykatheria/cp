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
        ll ar1[n],ar2[n];
        ll mn1=INT_MAX,mn2=INT_MAX;
        for(ll i=0;i<n;i++){
            cin>>ar1[i];
            mn1=min(mn1,ar1[i]);
        }
        for(ll i=0;i<n;i++){
            cin>>ar2[i];
            mn2=min(mn2,ar2[i]);
        }

        ll ans=0;

        for(ll i=0;i<n;i++){
            ans-=min(ar1[i]-mn1,ar2[i]-mn2);
            ans+=ar1[i]-mn1 + ar2[i]-mn2;
        }

        cout<<ans<<"\n";
    }
}

