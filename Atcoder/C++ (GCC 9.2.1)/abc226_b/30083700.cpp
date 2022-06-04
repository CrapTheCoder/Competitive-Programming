#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;
    set<string> result;

    for (int i = 0; i < n; i++) {
        int l; cin >> l;

        string s;
        for (int j = 0; j < l; j++) {
            string x; cin >> x;
            s += x + " ";
        }

        result.insert(s);
    }

    cout << result.size() << endl;
}
