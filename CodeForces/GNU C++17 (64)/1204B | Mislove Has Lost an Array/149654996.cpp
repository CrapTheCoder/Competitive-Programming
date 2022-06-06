#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ll n,l,r;
    cin>>n>>l>>r;
    ll val1=1;
    ll minsum=0;
    for(ll i=0;i<l;i++){
        minsum+=val1;
        val1*=2;
    }
    minsum+=n-l;
 
    ll maxsum=0;
    ll val2=1;
    for(ll i=0;i<r;i++){
        maxsum+=val2;
        val2*=2;
    }
    maxsum+=(n-r)*(val2/2);
 
    cout<<minsum<<" "<<maxsum<<endl;
}