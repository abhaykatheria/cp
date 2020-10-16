#include <iostream>
#include <bits/stdc++.h>
#define ll long long

using namespace std;


int main(){
    ll t,a,b,x,y,n;
    cin>>t;
    while(t--){
       cin>>a>>b>>x>>y>>n;

       if(a-x + b-y <n){
        cout<<x*y<<endl;
        continue;
       }


       ll temp1=a-min(a-x,n);
       ll temp2=b-(n-(a-temp1));

        ll ans1=temp1*temp2;
        if(ans1<0)
            ans1=INT_MAX;

        temp1=b-min(b-y,n);
        temp2=a-(n-(b-temp1));
        ll ans2=temp1*temp2;
       cout<<min(ans1,ans2)<<endl;

    }
}

 