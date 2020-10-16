#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll mod=1e9 + 7;

int32_t main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ll t,n,x,y,z,k;
    cin>>t;
    while(t--){
        cin>>n;
        multiset<int> ms;
        for(int i=1;i<=n;i++)
            ms.insert(i);
        cout<<2<<endl;

        while(!ms.empty()){
            x=*ms.rbegin();

            auto it=ms.lower_bound(x);
            ms.erase(it);

            if(ms.empty()) break;

            y=*ms.rbegin();
            it=ms.lower_bound(y);
            ms.erase(it);

            cout<<x<<" "<<y<<endl;

            ms.insert(ceil((x+y)/2.0));
        }



    }

}