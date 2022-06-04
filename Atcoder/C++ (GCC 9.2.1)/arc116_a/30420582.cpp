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
        int n; cin >> n;
        if (n % 4 == 0)
            cout << "Even" << endl;
        else if (n % 2 == 0)
            cout << "Same" << endl;
        else
            cout << "Odd" << endl;
    }
}
