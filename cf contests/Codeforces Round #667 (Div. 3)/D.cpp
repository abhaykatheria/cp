#include <iostream>
#include <bits/stdc++.h>
#define ll unsigned long long

using namespace std;

bool isSmaller(string str1, string str2)
{
    int n1 = str1.length(), n2 = str2.length();

    if (n1 < n2)
    return true;
    if (n2 < n1)
    return false;

    for (int i=0; i<n1; i++)
    if (str1[i] < str2[i])
        return true;
    else if (str1[i] > str2[i])
        return false;

    return false;
}


string findDiff(string str1, string str2)
{
    if (isSmaller(str1, str2))
        swap(str1, str2);

    string str = "";

    int n1 = str1.length(), n2 = str2.length();

    reverse(str1.begin(), str1.end());
    reverse(str2.begin(), str2.end());

    int carry = 0;

    for (int i=0; i<n2; i++)
    {

        int sub = ((str1[i]-'0')-(str2[i]-'0')-carry);

        if (sub < 0)
        {
            sub = sub + 10;
            carry = 1;
        }
        else
            carry = 0;

        str.push_back(sub + '0');
    }

    for (int i=n2; i<n1; i++)
    {
        int sub = ((str1[i]-'0') - carry);

        if (sub < 0)
        {
            sub = sub + 10;
            carry = 1;
        }
        else
            carry = 0;

        str.push_back(sub + '0');
    }

    reverse(str.begin(), str.end());

    return str;
}


int main(){
    ll t,n,k;
    cin>>t;
    while(t--){
       cin>>n>>k;

       string s=to_string(n);
       int sum=0;
       for(int i=0;i<s.length();i++)
            sum+=int(s[i]-'0');
       if(sum<=k){
        cout<<0<<endl;continue;
       }

       int index=0;
       sum=0;
       for(int i=0;i<s.length();i++){
        sum+=int(s[i]-'0');
        if(sum>=k){
            index=i-1;
            break;
        }
       }

       string s1="";

       if(index==-1){
        s1+="1";
       }
       else{
        for(int i=0;i<index;i++)
            s1+=s[i];
        s1+=(s[index]+1);
       }
       for(int i=index+1;i<s.length();i++)
        s1+="0";

        if(s.length()<s1.length()){
            string s2="0";
            s2+=s;
            s=s2;
        }
        string ans= findDiff(s,s1);

        int i=0;
        while(ans[i++]=='0'){

        }
        i--;
        for(;i<ans.length();i++)
            cout<<ans[i];
        cout<<endl;
    }
}

 