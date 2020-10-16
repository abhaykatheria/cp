#include <bits/stdc++.h>
using namespace std;

void subsetsUtil(vector<int>& A, vector<vector<int> >& res,
				vector<int>& subset, int index)
{
	res.push_back(subset);
	for (int i = index; i < A.size(); i++) {

		subset.push_back(A[i]);

		subsetsUtil(A, res, subset, i + 1);

		subset.pop_back();
	}

	return;
}

vector<vector<int> > subsets(vector<int>& A)
{
	vector<int> subset;
	vector<vector<int> > res;

	int index = 0;
	subsetsUtil(A, res, subset, index);

	return res;
}

int inv(vector<int> v){
    if(v.empty())
        return 0;
    int n=v.size();
    multiset<int> set1;
    set1.insert(v[0]);

    int invcount = 0;
    multiset<int>::iterator itset1;
    for (int i=1; i<n; i++)
    {
        set1.insert(v[i]);

        itset1 = set1.upper_bound(v[i]);

        invcount += distance(itset1, set1.end());
    }

    return invcount;
}

int main()
{
    int n,t;
    cin>>t;
    while(t--){
    cin>>n;
    vector<int> ar(n);
    for(int i=0;i<n;i++){
        cin>>ar[i];
    }
    int ans=0;
	vector<vector<int> > res = subsets(ar);
    for (int i = 0; i < res.size(); i++) {
        set<int> st;
		for (int j = 0; j < res[i].size(); j++){
			st.insert(res[i][j]);
		}
		vector<int> v;
		for(int j=0;j<n;j++)
            if(st.count(ar[j])==0)
                v.push_back(ar[j]);
		if(inv(v)==inv(res[i]))
            ans++;
        if(ans>0) break;
    }


    if(ans>0) cout<<"YES\n";
    else cout<<"NO\n";

}
}
