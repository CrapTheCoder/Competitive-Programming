#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define MAX 100010

int p[MAX];

set<int> pf(int n) {
    set<int> x;
    while (n != 1) {
        x.insert(p[n]);
        n /= p[n];
    }

    return x;
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    iota(p, p+MAX, 0);

    for (int i = 2; i*i < MAX; i++) if (p[i] == i)
        for (int j = i*i; j < MAX; j += i) if (p[j] == j)
            p[j] = i;

    int t; cin >> t;

    while (t--) {
        int n; cin >> n;
        map<int, int> c;
        set<int> ix[n];

        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            ix[i] = pf(x);

            for (auto j : ix[i])
                c[j]++;
        }

        map<int, int> m;

        for (int i = 0; i < n-1; i++) {
            for (auto j : ix[i]) {
                c[j]--; m[j]++;
            }

            bool flag = false;
            for (auto j : c) {
                if (c[j.first] > 0 && m[j.first] > 0) {
                    flag = true;
                    break;
                }
            }

            if (!flag) {
                cout << i+1 << endl;
                break;
            }
        }
    }
}
