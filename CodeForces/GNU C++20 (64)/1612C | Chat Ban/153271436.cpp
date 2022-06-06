#include<bits/stdc++.h>
#define int long long
using namespace std;
 
signed main()
{
    int t;
    cin>>t;
 
    while(t--)
    {
        int k,x;
        cin>>k>>x;
 
        if(k*k<=x)
            cout<<2*k-1;
 
        else if((k*(k+1))/2>=x)
        {
            long double ans=(sqrt(1+8*(long double)x)-1)/2;
            cout<<(int)ceil(ans);
        }
        else
        {
            x-=(k*(k+1))/2;
            int total=k*(k-1)-2*x;
            int ans=((int)sqrt(1+4*total)-1)/2;
            cout<<(int)2*k-1-ans;
        }
        cout<<"\n";
    }
}