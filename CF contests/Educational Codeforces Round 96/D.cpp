#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll mod=1e9 + 7;


int32_t main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    int n,t;
    cin>>t;
    while(t--){
    cin>>n;
    string s;
    cin>>s;

    vector<int> pre;
    int cnt=0;
    for(int i=0;i<n-1;i++){
        if(s[i]==s[i+1])
            cnt++;
        else{
            pre.push_back(cnt+1);
            cnt=0;
        }
    }
    pre.push_back(cnt+1);

//    for(int i=0;i<pre.size();i++)
//        cout<<pre[i]<<" ";
//    cout<<endl;

    int i1=0,i2=0;
    int ans=0;
    while(i1<pre.size()){
        ans++;



        if(pre[i1]>1){
            pre[i1]=0;
            i1++;
        }
        else{
            pre[i1]=0;
            i1++;
            while(i2<pre.size() && pre[i2]<=1)
                i2++;
            if(i2==pre.size()){
                int cnt=0;
                for(int i=0;i<pre.size();i++)
                    if(pre[i]==1)
                        cnt++;
                ans+=floor(cnt/2.0);
                break;

            }
            pre[i2]--;

        }
    }

    cout<<ans<<endl;

}
}