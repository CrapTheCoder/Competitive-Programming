#include <bits/stdc++.h>

using namespace std;

#define endl '\n'
#define int long long

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m; cin >> n >> m;
    int d[n]; fill(d, d+n, -1);

    for (int i = 0; i < m; i++) {
        int a, b; cin >> a >> b;
        a--; b--;

        while (d[a] >= 0) a = d[a];
        while (d[b] >= 0) b = d[b];

        if (a < b)
            swap(a, b);

        if (a != b) {
            d[a] += d[b];
            d[b] = a;
        }
    }

    vector<int> l;
    int s = 0;

    for (int i = 0; i < n; i++) {
        if (d[i] < 0) {
            l.push_back(-d[i]);
            s += -d[i];
        }
    }

    int f = 0;
    for (auto i : l)
        f += i * (s-i);

    cout << f / 2 << endl;
}
