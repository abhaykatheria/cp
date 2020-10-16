#include <bits/stdc++.h>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (int) n; i++)
#define PB push_back
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define F first
#define S second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;


int main(){
	ios::sync_with_stdio(false); cin.tie(0);

    ll n;
    cin>>n;
    ll ar[n];
    ll prefix[n];
    for(ll i=0;i<n;i++){
        cin>>ar[i];
        if(i==0)
            prefix[i]=ar[i];
        else
            prefix[i]=ar[i]+prefix[i-1];
    }

    ll ans=0;
    ll mod=1e9 + 7;


    for(ll i=0;i<n;i++){
        ll sum=prefix[n-1]-prefix[i];
        sum=sum%mod;
        ans+=(sum*ar[i]);
        ans=ans%mod;
    }
    cout<<ans<<endl;
}

