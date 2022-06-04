#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
#define ld long double
using namespace std;
const int MOD = 1e9 + 7;
const int N = 100003;
long long int pre[N], num[N];

ll power(ll x, ll y){
    x %= MOD;
    ll ans = 1;
    while(y){
        if(y & 1)
            ans = (ans * x) % MOD;
        y >>= 1LL;
        x = (x * x) % MOD;
    }
    return ans;
}

void solve(){
    int l, r;
    cin >> l >> r;
    long long exponent = pre[r] - pre[l];
    long long ans = power(num[l], exponent);
    cout << ans << '\n';
}

int main() {
    fast;

    for(int i = 1; i < N; ++i){
        if(i <= 9){
            pre[i] = (pre[i - 1] + i) % MOD;
            num[i] = i;
        }
        else {
            string s = to_string(i);
            int extract = s.size() - 1;
            string cur;
            for(int j = extract - 1; j >= 0; --j) cur.push_back(s[j]);
            s += cur;
            long long x = stoll(s);
            pre[i] = (pre[i - 1] + x) ;
            num[i] = x;
        }
    }

    int t = 1;
    cin >> t;
    while(t--)
        solve();
    return 0;
}
