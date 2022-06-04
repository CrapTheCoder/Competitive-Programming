#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define INF INT_MAX

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, t; cin >> n >> t;

    int a[n+1];
    for(int i = 0; i < n; i++)
        cin >> a[i];

    a[n] = INT_MAX;

    int j = 0;
    int s = 0;
    int d = 0;

    for (int i = 0; i < n; i++) {
        while ((j <= n) && (s <= t)) {
            s += a[j];
            j++;
        }

        int x = j - i - 1;
        d += x;

        s -= a[i];
    }

    cout << setprecision(6) << (float) d / (n * (n+1) / 2) << endl;
}
