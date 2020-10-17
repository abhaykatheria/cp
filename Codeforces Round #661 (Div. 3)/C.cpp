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
        ll ar[n];
        for(ll i=0;i<n;i++){
            cin>>ar[i];
        }
        sort(ar,ar+n);
        ll ans=0,cnt=0;




        for(ll weight=ar[0]+ar[1];weight<=ar[n-1]+ar[n-2];weight++){
            cnt=0;
            map<ll,ll> mp;
            for(ll i=0;i<n;i++)
                mp[ar[i]]++;

            for(ll i=0;i<n;i++){
                if(mp[weight-ar[i]]>0&&mp[ar[i]]>0 && ar[i]!=weight-ar[i]){
                    cnt++;
                    mp[ar[i]]--;
                    mp[weight-ar[i]]--;
                }
                if(weight==ar[i]*2 && mp[ar[i]]>1){
                    cnt++;
                    mp[ar[i]]--;
                    mp[weight-ar[i]]--;
                }
            }

            ans=max(ans,cnt);
            //cout<<weight<<" "<<cnt<<endl;
        }
        cout<<ans<<"\n";
    }
}

