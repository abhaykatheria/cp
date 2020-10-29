#include<bits/stdc++.h>
using namespace std;

// minimum distance

vector<pair<int,int>> *g;

int v,e;

int minm(int dist[], bool vis[]) {
    int min = INT_MAX,ind;
    for(int i=0;i<v;i++) {
        if(!vis[i] && dist[i] < min) {
            min = dist[i];
            ind = i;
        }
    }
    return ind;
}

void dijkstra(int src) {
    int dist[v];
    bool vis[v];
    int parent[v];
    for(int i=0;i<v;i++) { dist[i] = INT_MAX; vis[i] = false; }
    dist[src] = 0;
    parent[src] = -1;
    int n;
    int i=0;
    while(i < v) {
        i++;
        n = minm(dist,vis);
        vis[n] = true;
        for(auto x:g[n]) {
            if(!vis[x.first] && (x.second + dist[n]) < dist[x.first]) {
                dist[x.first] = x.second + dist[n];
                parent[x.first] = n;
            }
        }
    }
    cout<<"nodes    |    dist\n";
    for(int i=0;i<v;i++) {
        cout<<parent[i]<<"  "<<i<<"    |   "<<dist[i]<<"\n";
    }
}

int main() {
    cin>>v>>e;
    g = new vector<pair<int,int>>[v];
    int a,b,w;
    for(int i=0;i<e;i++) {
        cin>>a>>b>>w;
        g[a].push_back({b,w});
        g[b].push_back({a,w});
    }
    dijkstra(0);
}