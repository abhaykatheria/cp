#include<bits/stdc++.h>
using namespace std;
// TREE
struct Node {
    int info;
    struct Node *l,*r;
};
typedef struct Node node;


void itervative_inorder_stack(node* root);
void root_to_leaf(node *root);
int sum_binary_tree(node *root);

// insert
//traversal
// min element
// delete
// height
// diagonal
// mirror
// check foldable
// max width
// iterative inorder with stack
// sum_binarytree


node * insert(node* root, int x) {
    if(root == NULL) {
        node * n = (node*) malloc (sizeof(node));
        n->info = x;
        n->l = NULL; n->r = NULL;
        return n;
    }
    if(root->info < x) 
        root->r = insert(root->r,x);
    else if(root->info > x)
        root->l = insert(root->l,x);
    else
        return root;
    return root;
}

void traversal(node * root) {
    if(root) {
        traversal(root->l);
        cout<<root->info<<" ";
        traversal(root->r);
    }
}

node * minelement(node * root) {
    while(root && root->l)
        root = root->l;
    return root;
}

node * del_this(node* root, int x) {
    if(!root)
        return root;
    if(root->info < x)
        root->r = del_this(root->r,x);
    else if (root->info > x)
        root->l = del_this(root->l,x);
    else {
        if(root->l == NULL) {
            node * temp = root->r;
            free(root);
            return temp;
        }
        if(root->r == NULL) {
            node * temp = root->l;
            free(root);
            return temp;
        }
        node * temp = minelement(root->r);
        root->info = temp->info;
        temp->info = x;
        root->r = del_this(root->r,x);
        return root;
    }
    return root;
}

int height(node * root) {
    if(!root)
        return 0;
    int lheight = height(root->l);
    int rheight = height(root->r);
    if(lheight > rheight)
        return lheight + 1;
    else
        return rheight + 1;
}

int diagonal(node * root) {
    if(!root)
        return 0;
    int lheight = diagonal(root->l);
    int rheight = diagonal(root->r);
    int ldia = diagonal(root->l);
    int rdia = diagonal(root->r);
    return max(lheight+rheight+1 , max(ldia,rdia));
}

node * mirror(node * root) {
    if(!root)
        return root;
    root->l = mirror(root->l);
    root->r = mirror(root->r);
    node * temp = root->l;
    root->l = root->r;
    root->r = temp;
    return root;
}

bool check_foldable(node* n1,node* n2) {
    if(!n1 && !n2)
        return true;
    if(!n1 || !n2)
        return false;
    return check_foldable(n1->l,n2->r) && check_foldable(n1->r,n2->l);
}

bool is_foldable(node * root) {
    if(!root)
        return true;
    return check_foldable(root->l,root->r);
}

void max_width(node * root, int *a,int level) {
    if(root) {
        a[level]++;
        max_width(root->l,a,level+1);
        max_width(root->r,a,level+1);
    }
}

int find_max_width(node * root) {
    int h = height(root);
    int a[h] = {0};
    int level = 0;
    max_width(root,a,level);
    int m = a[0];
    for(int i=1;i<h;i++)
        if(m < a[i])
            m = a[i];
    return m;
}
// dont use this function use below one at the end
node* travel_Iterate(node *root ) {
    if(!root) return root;
    stack<node *> s;
    node *prev = NULL;
    node *m = NULL;
    do {
        while(root) {
            s.push(root);
            root = root->l;
        }
        root = s.top();
        s.pop();
        //cout<<root->info<<" "; // root->l
        if(m == NULL) m = root;
        root->l = prev;
        if(prev != NULL) {prev->r = root;}
        prev = root;
        root = root->r;
        if(root) {s.push(root); root = root->l;}
    }while(!s.empty());
    return m;
}




int main() {
    node * root=NULL;
    cout<<"yes";
    root = insert(root, 5);
    root = insert(root, 3);
    root = insert(root, 10);
    root = insert(root, 1);
    root = insert(root, 2);
    root = insert(root, 7);
    root = insert(root, 8);
    root = insert(root, 6);
    root = insert(root, 9);
    cout<<"traversal\n";
    traversal(root);
    cout<<"\nsum_binary_tree: ";
    sum_binary_tree(root);
    traversal(root);
    cout<<"\n";
    cout<<"height: " << height(root)<<"\n";
    cout<<"diagonal: " << diagonal(root)<<"\n";
    cout<<"foldable: "<< is_foldable(root) <<"\n";
    cout<<"max Width: "<< find_max_width(root)<<"\n";
        cout<<"\n iterative inorder: ";
    itervative_inorder_stack(root);
    cout<<"\n";
    root = mirror(root);
    cout<<"mirror: ";
    traversal(root);
    root = mirror(root);
    cout<<"\n";
    root= del_this(root, 7);
    traversal(root);
    cout<<"\n";
    cout<<"Iterative: ";
    root = travel_Iterate(root);
    node *k = root;
    while (root)
    {
        cout<<root->info<<" ";
        if(root->r == NULL) break;
        root = root->r;
    }
    cout<<"\n";
    while(root) {
        cout<<root->info<<" ";
        root = root->l;
    }
    root = k;
    
}



void itervative_inorder_stack(node* root) {
    if(root) {
        stack<node*> s;
        s.push(root);
        while(!s.empty()) {
            while(root && root->l != NULL) {
                s.push(root->l);
                root = root->l;
            }
            root = s.top();
            s.pop();
            cout<<root->info<<" ";
            if(root->r != NULL){
                s.push(root->r);
                root = root->r;
            }
            else root = NULL;
        }
    }
}

void root_to_leaf(node *root)  {
    if(!root) return ;
    vector<int> v;
    stack<node*> s;

    s.push(root);
    while(!s.empty()) {
        auto x = s.top();
        s.pop();
        if(x->l != NULL) s.push(x->l);
        if(x->r != NULL) s.push(x->r);
    }
}


int sum_binary_tree(node *root) {
    if(root == NULL) return 0;
    int a = root->info;

    root->info = sum_binary_tree(root->l) + sum_binary_tree(root->r);
    return a + root->info ; 
}












