#include <bits/stdc++.h>

using namespace std;

#define FOR(i, n) for(int i = 0; i < (int) n; i++)
#define PB push_back
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define F first
#define S second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;


int main(){
	ios::sync_with_stdio(false); cin.tie(0);

    string s1,s2;
    int mn=INT_MAX,curr=0;
    cin>>s1>>s2;
    for(int i=0;i<=s1.length()-s2.length();i++){
        curr=0;
        for(int j=i;j<i+s2.length();j++){
            if(s2[j-i]!=s1[j])
                curr++;
            //cout<<s1[j];
        }
        //cout<<endl;
        mn=min(mn,curr);
    }
    cout<<mn<<endl;
}

