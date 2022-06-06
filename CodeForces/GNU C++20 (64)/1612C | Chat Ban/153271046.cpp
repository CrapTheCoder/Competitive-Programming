#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
 
    ll t, k, x, ans, l, c;
    long double x1, ans1;
    cin>>t;
 
    for(;t--;)
    {
        cin>>k>>x;
 
        c=k*k;
 
        if(c<=x){
            cout<<2*k-1<<"\n";
            continue;
        }
 
        c=(k*(k+1))/2;
 
        if(c<=x){
            x=x-c;
            x=(k*(k-1))/2-x;
 
 
            x1=x;
 
            ans1=floor((sqrt(1+8*x)-1)/2);
 
            ans=2*k-1-ans1;
 
            cout<<ans<<"\n";
        }else{
 
            x1=x;
 
            ans1=ceil((sqrt(1+8*x1)-1)/2);
 
            ans=ans1;
 
            cout<<ans<<"\n";
 
        }
    }
}