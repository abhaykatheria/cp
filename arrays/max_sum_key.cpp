#include<bits/stdc++.h>
using namespace std;

vector<vector<int>> g;

struct Node {
    int key;
    vector<Node*> child;
};
typedef struct Node node;

Node* newNode(int key) {
    node *temp = new Node;
    temp->key = key;
    return temp;
}

int maxSum(node *root) {
    queue<node*> q;
    q.push(root);
    vector<pair<int,int>> p;
    int pr,c;
    while(!q.empty()) {
        auto y = q.front();
        q.pop();
        pr = y->key;
        c = y->key;
        for(auto x:(y->child)) {
            q.push(x);
            c += x->key;
        }
        p.push_back({pr,c});
    }
    int n = p.size();
    auto j = p[0];
    for(int i=0;i<n;i++) {
        if(j.second < p[i].second) {
            j.second = p[i].second;
            j.first = p[i].first;
        }
    }
    return j.first;
}

int main() {
    node* root = newNode(1);
    (root->child).push_back(newNode(2)); 
    (root->child).push_back(newNode(3)); 
    (root->child).push_back(newNode(4)); 
    (root->child[0]->child).push_back(newNode(5)); 
    (root->child[0]->child).push_back(newNode(6)); 
    (root->child[2]->child).push_back(newNode(5)); 
    (root->child[2]->child).push_back(newNode(6)); 
    (root->child[2]->child).push_back(newNode(6));
    cout<<maxSum(root) <<"\n";
}

