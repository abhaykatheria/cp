#include <iostream>
#include <bits/stdc++.h>
#define ll long long

using namespace std;

ll mod=998244353;

vector<vector<int>> adj;
vector<int> indeg;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t,n,u,v;
    cin>>t;
    while(t--){
        cin>>n;
        adj.clear();indeg.clear();
        adj.resize(n);indeg.resize(n);
        indeg.assign(n,0);
        for(int i=1;i<n;i++){
            cin>>u>>v;
            u--;
            v--;
            adj[u].push_back(v);
            indeg[v]++;
        }
        int cnt=0;
        for(int i=0;i<n;i++)
            if(indeg[i]==0)
                cnt++;
        cout<<cnt-1<<endl;

    }

}
