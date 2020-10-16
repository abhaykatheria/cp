#include <bits/stdc++.h>

using namespace std;

#define int long long

vector<int> graph[200005];
void add_edge(int u, int v)
{
    graph[u].push_back(v);
    graph[v].push_back(u);
}

// Function to traverse the undirected graph
// using DFS algorithm and keep a track of
// individual lengths of connected chains
void depthFirst(int v, vector<int> graph[],
                vector<bool>& visited, int& ans)
{
    // Marking the visited vertex as true
    visited[v] = true;

    // Incrementing the count of
    // connected chain length
    ans++;

    for (auto i : graph[v]) {
        if (visited[i] == false) {
            // Recursive call to the DFS algorithm
            depthFirst(i, graph, visited, ans);
        }
    }
}

// Function to initialize the graph
// and display the result
int UniqueConnectedComponent(int n,
                              vector<int> graph[])
{
    int mx = -1 ;

    // Initializing boolean visited array
    // to mark visited vertices
    vector<bool> visited(n + 1, false);

    // Initializing a Set container
    unordered_set<int> result;

    // Following loop invokes DFS algorithm
    for (int i = 1; i <= n; i++) {
        if (visited[i] == false) {
            // ans variable stores the
            // individual counts
            int ans = 0;

            // DFS algorithm
            depthFirst(i, graph, visited, ans);

            // Inserting the counts of connected
            // components in set
            result.insert(ans);
            mx = max (mx,ans);
        }
    }
    return mx ;
}
int32_t  main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,m;
    cin >> n >> m;
    for(int i=0;i<m;i++){
        int a,b;
        cin >>a>>b;
        add_edge(a,b);
    }
    cout << UniqueConnectedComponent(n,graph);
    return 0;
}