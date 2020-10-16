#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll mod=1e9 + 7;

ll merge(ll arr[], ll temp[], ll left, ll mid, ll right)
{
    ll inv_count = 0;

    ll i = left; 
    ll j = mid;  
    ll k = left; 
    while ((i <= mid - 1) && (j <= right))
    {
        if (arr[i] <= arr[j])
            temp[k++] = arr[i++];
        else
        {
            temp[k++] = arr[j++];

            inv_count = inv_count + (mid - i);
        }
    }

     (if there are any) to temp*/
    while (i <= mid - 1)
        temp[k++] = arr[i++];

     (if there are any) to temp*/
    while (j <= right)
        temp[k++] = arr[j++];

    for (i=left; i <= right; i++)
        arr[i] = temp[i];

    return inv_count;
}

ll _mergeSort(ll arr[], ll temp[], ll left, ll right)
{
    ll mid, inv_count = 0;
    if (right > left)
    {
        mid = (right + left)/2;
        inv_count  = _mergeSort(arr, temp, left, mid);
        inv_count += _mergeSort(arr, temp, mid+1, right);

        inv_count += merge(arr, temp, left, mid+1, right);
    }

    return inv_count;
}

ll countSwaps(ll arr[], ll n)
{
    ll temp[n];
    return _mergeSort(arr, temp, 0, n - 1);
}



int32_t main(){
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    ll n;
    cin>>n;

    string s;
    cin>>s;
    reverse(s.begin(),s.end());
    map<char,queue<ll>> mp;

    if(mp.size()==n){
        cout<<n*(n-1)/2<<endl;
        return 0;
    }


    for(ll i=0;i<n;i++)
        mp[s[i]].push(i+1);

    reverse(s.begin(),s.end());

    vector<ll> v;

    for(ll i=0;i<s.length();i++){

        ll temp=mp[s[i]].front();
        mp[s[i]].pop();
        v.push_back(temp);
//        cout<<temp<<" ";
    }

    ll ar[n];

    for(ll i=0;i<n;i++)
        ar[i]=v[i];

    cout<<countSwaps(ar,n)<<endl;

}
 