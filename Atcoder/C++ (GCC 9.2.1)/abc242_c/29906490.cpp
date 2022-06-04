#include <bits/stdc++.h>
using namespace std;

#define int long long
const int MOD = 998244353;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int a[n+1][10];
    for (int j = 1; j <= 9; j++)
        a[1][j] = 1;

    for (int i = 2; i <= n; i++) {
        for (int j = 1; j <= 9; j++) {
            a[i][j] = a[i-1][j];
            if (1 <= j-1) a[i][j] += a[i-1][j-1];
            if (j+1 <= 9) a[i][j] += a[i-1][j+1];

            a[i][j] %= MOD;
        }
    }

    int s = 0;
    for (int j = 1; j <= 9; j++)
        s = (s + a[n][j]) % MOD;

    cout << s << endl;
}
