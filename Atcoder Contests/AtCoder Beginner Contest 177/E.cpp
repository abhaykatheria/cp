#include <bits/stdc++.h>
#define MAXN   1000001
using namespace std;

typedef long long ll;

int spf[MAXN];

void sieve()
{
    spf[1] = 1;
    for (int i=2; i<MAXN; i++)

        spf[i] = i;

    for (int i=4; i<MAXN; i+=2)
        spf[i] = 2;

    for (int i=3; i*i<MAXN; i++)
    {

        if (spf[i] == i)
        {

            for (int j=i*i; j<MAXN; j+=i)


                if (spf[j]==j)
                    spf[j] = i;
        }
    }
}


int main(){
	ios::sync_with_stdio(false); cin.tie(0);
    sieve();
    int n;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++)
        cin>>ar[i];

    map<int,int> mp;
    int gcd=0;
    for(int i=0;i<n;i++){
        gcd=__gcd(gcd,ar[i]);
        int temp=ar[i];
        map<int,int> mp1;
        while(temp!=1){
            mp1[spf[temp]]++;
            //cout<<temp<<endl;
            while(temp%spf[temp]==0 && temp>1){
                temp/=spf[temp];
                mp1[spf[temp]]++;
               // cout<<temp<<endl;
            }

        }
        for(auto it: mp1)
            mp[it.first]++;
    }
    int flag=1;
    

    for(auto it: mp)
        if(it.second>1 && it.first!=1){
            flag=0;break;
        }
    if(flag && gcd==1){
        cout<<"pairwise coprime"<<endl;
        return 0;
    }
    if(flag)
        cout<<"pairwise coprime"<<endl;
    else if(gcd==1)
        cout<<"setwise coprime"<<endl;
    else
        cout<<"not coprime"<<endl;
}

