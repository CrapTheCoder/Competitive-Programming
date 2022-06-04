#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define int long long
#define endl '\n'

main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    int f[100013];
    f[0] = 1;

    for (int i = 1; i < 100013; i++)
        f[i] = (f[i-1] * i) % MOD;

    while (t--) {
        int n; cin >> n;

        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];

        stack<pair<int, int>> c;
        int maxi = 1;

        for (int i = 0; i < n; i++) {
            int li = i;

            while (!c.empty() && c.top().first <= a[i]) {
                li = c.top().second;
                c.pop();
            }

            c.push({a[i], li});

            maxi = max(maxi, i - li);
        }

        cout << f[maxi+1] << endl;
    }
}
