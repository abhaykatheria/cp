#include <iostream>
#include <bits/stdc++.h>
#define ll long long

using namespace std;


int main(){
    ll t,a,b,x,y,n;
    cin>>t;
    while(t--){
        cin>>n>>x>>y;
        ll diff=y-x;

        ll d=y-x;
        for(ll i=n-1;i>=1;i--){
            if(diff%i==0){
                d=diff/i;
                break;
            }
        }

        vector<int> v;
        for(int i=x;i<=y;i+=d){
            v.push_back(i);
        }
        for(int i=x-d;i>0;i-=d){
            if(v.size()==n)
                break;
            v.push_back(i);
        }
        for(int i=y+d;;i+=d){
            if(v.size()==n)
                break;
            v.push_back(i);
        }
        for(int i=0;i<n;i++)
            cout<<v[i]<<" ";
        cout<<endl;
    }
}

 