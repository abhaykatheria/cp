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
        cin>>n;
        int ar[n];
        for(int i=0;i<n;i++)
            cin>>ar[i];
        int flag=1;
        for(int i=0;i<n;i++){
            if((i+1)%ar[i]==0)
                continue;
            else{
                flag=0;break;
            }
        }
        if(flag) cout<<"YES\n";
        else cout<<"NO\n";
    }

}
