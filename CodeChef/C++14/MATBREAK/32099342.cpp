#include<bits/stdc++.h>
#define faster ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL)
using namespace std;
int MOD=1000000007;
long long powe(long long res,long long n)
{    if (res==0)
         return 0;
    if (n==0)
        return 1;
    long long tem=powe(res,n/2);
     if (n%2==1)
        return ((res*((tem*tem)%MOD))%MOD);
    else
        return ((tem*tem)%MOD);
}

signed main()
{
   faster;
   #ifndef ONLINE_JUDGE
     freopen("ip.txt", "r", stdin);
     freopen("op.txt", "w", stdout);
   #endif
     int t;cin>>t;
     while(t--)
     {
        int n,a;
        cin>>n>>a;
        long long res=a,rem=0,tem;
        for (int i=1;i<=n;i++)
        {
            tem=(powe(res,2*i-1))%MOD;
            rem=(rem+tem)%MOD;
            res=(res*tem)%MOD;
            // cout<<tem<<endl;
            // cout<<res<<endl;
        }
        cout<<rem<<endl;
     }
}