#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int power_mod(int a, int b, int mod=MOD) {
    a %= mod;

    int c = 1;
    while (b) {
        if (b & 1)
            c = (c * a) % mod;
        
        a = (a * a) % mod;
        b >>= 1;
    }

    return c;
}

int inverse(int a, int mod=MOD) {
    return power_mod(a, mod - 2, mod);
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n, m, p;
        cin >> n >> m >> p;

        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        
        unordered_map<int, int> b;
        for (int i = 0; i < m; i++) {
            int x; cin >> x;
            b[x]++;
        }
        
        int c = 0;
        for (int i = 0; i < n; i++)
            if (a[i] % p != 0)
                c += b[a[i] ^ inverse(a[i], p)];
        
        cout << c << endl;
    }
}
