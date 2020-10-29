#include<bits/stdc++.h>
using namespace std;

int main() {
    int t,n,k;
    cin>>t;
    while(t--) {
        cin>>k>>n;
        priority_queue<int,vector<int>,greater<int>> pq;
        int i=0;
        int a;
        while(i++<n) {
            cin>>a;
            if(pq.size() < k) {
                pq.push(a);
                if(pq.size() == k) cout<<pq.top()<<" ";
                else cout<<"-1 ";
            }
            else if(pq.size() == k && pq.top() >= a) cout<<pq.top()<<" ";
            else {
                pq.pop();
                pq.push(a);
                cout<<pq.top()<<" ";
            }
        }
        cout<<"\n";
    }
}

/*  // this code also correct with mean heap
#include<bits/stdc++.h>
using namespace std;

void heapify(int a[],int n,int i) {
    int p = i;
    int l = 2*i+1;
    int r = 2*i+2;
    if(l < n && a[l] < a[i]) 
        i = l;
    if(r < n && a[r] < a[i])
        i = r;
    if(p!=i) {
        a[i]^=a[p]^=a[i]^=a[p];
        heapify(a,n,i);
    }
}

void make_heap(int a[],int n) {
    for(int i=n/2-1;i>=0;i--)
        heapify(a,n,i);
}

int main() {
	int t;
	cin>>t;
	int k,n;
	while(t--) {
	    cin>>k>>n;
	    int a[n];
	    int t[k];
	    for(int i=0;i<n;i++){
	        cin>>a[i];
	        if(i < k)
	            t[i] = a[i];
	    } 
	    make_heap(t,k);
        for(int i=0;i<n;i++) {
            if(i < k-1)   cout<<-1<<" ";
            else if(i == k-1) cout<<t[0]<<" ";
            else {
                if(a[i] > t[0]) {
                    t[0] = a[i];
                    heapify(t,k,0);
                    cout<<t[0]<<" ";
                }
                else
                    cout<<t[0]<<" ";
            }
        }
        cout<<"\n";
	}
	return 0;
}
*/