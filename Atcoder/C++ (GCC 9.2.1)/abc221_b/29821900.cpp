#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    string a, b;
    cin >> a >> b;

    if (a == b) {
        cout << "Yes" << endl;
        return 0;
    }

    for (int i = 0; i < a.size() - 1; i++) {
        swap(a[i], a[i+1]);

        if (a == b) {
            cout << "Yes" << endl;
            return 0;
        }

        swap(a[i], a[i+1]);
    }

    cout << "No" << endl;
}
