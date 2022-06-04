#include<bits/stdc++.h>
using namespace std;
typedef string str;
typedef long long ll;
#define pb push_back
#define fast ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);//FAST IO
void init_code()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif // ONLINE_JUDGE
}
ll m=1000000007;
ll binpow(ll a, ll b)
{
    a%=m;
    ll res=1;
    while(b>0)
    {
        if(b&1)
        {
            res=(res*a)%m;
        }
        a=(a*a)%m;
        b>>=1;
    }
    return res;
}
vector<ll> dp(150010);
//dp[i]=number of non periodic string of length i
int main()
{
   ll n;
   cin >> n >> m;
    dp[1]=2;
    for(ll i=2;i<=n+1;i++)
    {
        dp[i]=binpow(2,i);
        for(ll j=1;j*j<=i;j++)
        {
            if(i%j==0)
            {
                dp[i]=(((dp[i]-dp[j])%m)+m)%m;
                if(i!=(i/j) && j!=(i/j))
                {
                    dp[i]=(((dp[i]-dp[i/j])%m)+m)%m;
                }
            }
        }
    }
    cout << dp[n];
}
