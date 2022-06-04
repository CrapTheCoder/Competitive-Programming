#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        int n, k; cin >> n >> k;
        string s; cin >> s;

        vector<int> v;
        for (int i = 0; i < n; i++)
            (!v.empty() && s[v.back()] != s[i]) ? v.pop_back() : v.push_back(i);
        
        string r(n, '0'); r[0] = '1';
        for (int i = k; i < v.size(); i += k)
            r[v[i]] = '1';
        
        cout << r << endl;
    }
}
