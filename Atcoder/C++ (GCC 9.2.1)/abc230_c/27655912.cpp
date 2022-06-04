#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int MAX = 1e6 + 13;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, a, b; cin >> n >> a >> b;
    int p, q, r, s; cin >> p >> q >> r >> s;

    for (int i = p; i <= q; i++) {
        for (int j = r; j <= s; j++) {
            if (i - a == j - b) {
                int k = i - a;
                if (max(1 - a, 1 - b) <= k && k <= min(n-a, n-b))
                    cout << "#";
                else
                    cout << ".";

            } else if (i - a == b - j) {
                int k = i - a;
                if (max(1 - a, b - n) <= k && k <= min(n - a, b - 1))
                    cout << "#";
                else
                    cout << ".";

            } else
                cout << ".";
        }

        cout << endl;
    }
}
