#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll mod=1e9 + 7;

int32_t main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int t,n,x,y,z;
    cin>>t;
    while(t--){
        cin>>n;

        x=0,y=0,z=0;

        for(int i=0;i<=n;i++){
            for(int j=0;j<=n;j++){
                int temp=i*3 + j*5;
                temp=n-temp;
                if(temp<0) break;
                
                if(temp%7==0){
                    x=i,y=j,z=temp/7;
                    break;
                }
                
            }
        }
        if(x==0 && y==0 && z==0)
            cout<<-1<<endl;
        else
            cout<<x<<" "<<y<<" "<<z<<endl;
    }

}