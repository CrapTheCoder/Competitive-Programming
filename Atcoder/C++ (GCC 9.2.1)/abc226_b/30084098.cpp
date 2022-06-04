#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    set<vector<int>> result;

    for (int i = 0; i < n; i++) {
        int l; cin >> l;

        vector<int> x(l);
        for (int j = 0; j < l; j++)
            cin >> x[j];

        result.insert(x);
    }

    cout << result.size() << endl;
}
