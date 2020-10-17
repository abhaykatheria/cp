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
        string s;
        cin>>s;
        int ar[n];
        vector<vector<int>> v(2);

        int k=0;

        for(int i=0;i<n;i++){
            if(s[i]=='0'){
                if(v[1].size()==0){
                    k++;
                    v[0].push_back(k);
                    ar[i]=k;
                }
                else{
                    v[0].push_back(v[1][0]);
                    ar[i]=v[1][0];
                    v[1].erase(v[1].begin());
                }
            }
            else{
                if(v[0].size()==0){
                    k++;
                    v[1].push_back(k);
                    ar[i]=k;
                }
                else{
                    v[1].push_back(v[0][0]);
                    ar[i]=v[0][0];
                    v[0].erase(v[0].begin());
                }
            }
        }
        cout<<k<<endl;
        for(int i=0;i<n;i++)
            cout<<ar[i]<<" ";


        cout<<endl;
    }
}

