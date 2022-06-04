#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        string n; cin >> n;

        if ((n.back() - '0') % 2 == 1) {
            bool odd_exists = false;
            for (int i = 0; i < n.size() - 1; i++)
                if ((n[i] - '0') % 2 == 1)
                    odd_exists = true;

            if (odd_exists)
                cout << "YES" << endl;
            else
                cout << "NO" << endl;

        } else {
            bool even_exists = false;
            for (int i = 0; i < n.size() - 1; i++)
                if ((n[i] - '0') % 2 == 0)
                    even_exists = true;

            if (even_exists)
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }
    }
}
