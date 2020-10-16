#include <iostream>
#include <bits/stdc++.h>
#define ll long long

using namespace std;

ll mod=998244353;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t,n;
    cin>>t;
    while(t--){
        int sum=0;
        cin>>n;
        while(n--){
            int temp;cin>>temp;
            sum+=temp;
        }
        if(sum<0) cout<<"NO\n";
        else cout<<"YES\n";
    }

}
