#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
int solve(vector<int> a, int cur) {
    int n = a.size();
    int count = 0;
 
    int i0 = 0, i1 = 0;
    for (int i = 0; i < n; i++) {
        while (i0 < n && a[i0] != 0) i0++;
        while (i1 < n && a[i1] != 1) i1++;
 
        if (cur == 0)
            count += abs(i - i0++);
        else
            count += abs(i - i1++);
 
        cur ^= 1;
    }
 
    return count / 2;
}
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n; cin >> n;
        int c0 = 0, c1 = 0;
 
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            a[i] %= 2;
 
            (a[i] == 1) ? c1++ : c0++;
        }
 
        if (abs(c0 - c1) > 1) {
            cout << -1 << endl;
            continue;
        }
 
        if (n % 2) {
            if (c0 > c1)
                cout << solve(a, 0) << endl;
            else
                cout << solve(a, 1) << endl;
 
        } else {
            cout << min(solve(a, 0), solve(a, 1)) << endl;
        }
    }
}