#include <iostream>
#include <bits/stdc++.h>

using namespace std;


int main(){
    int t,a,b;
    cin>>t;
    while(t--){
        cin>>a>>b;
        int diff=abs(a-b);
        cout<<(int)ceil(diff/10.0)<<"\n";
    }
}

 