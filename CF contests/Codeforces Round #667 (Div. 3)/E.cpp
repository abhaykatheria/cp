#include <iostream>
#include <bits/stdc++.h>
#define ll unsigned long long

using namespace std;

int main(){
    ll t,n,k;
    cin>>t;
    while(t--){
       cin>>n>>k;

       ll ar[n];
       for(ll i=0;i<n;i++)
        cin>>ar[i];
       for(ll i=0;i<n;i++){
        int temp;
        cin>>temp;
       }

        sort(ar,ar+n);

        vector<pair<int,int>> v;
        map<int,int> mp;



        for(int i=0;i<n;i++){
            if(mp[ar[i]]!=0)
                continue;
            int cnt=upper_bound(ar,ar+n,ar[i]+k)-ar;

            cnt-=i;

            v.push_back(make_pair(ar[i],cnt));

            mp[ar[i]]=1;
        }

        int mx[v.size()+1]={0};
        int mm=0;
        for(int i=v.size()-1;i>=0;i--){
            mm=max(mm,v[i].second);
            mx[i]=mm;
        }
        mx[v.size()]=0;
        int ans=0;

        vector<int> v1;
        for(int i=0;i<v.size();i++){
            v1.push_back(v[i].first);
        }
        for(int i=0;i<v.size();i++){
            int curr=v[i].second;
            int index=upper_bound(v1.begin(),v1.end(),v[i].first+k)-v1.begin();
            if(index!=i)
            curr+=mx[index];
            ans=max(ans,curr);
        }

       cout<<ans<<endl;

    }
}

 