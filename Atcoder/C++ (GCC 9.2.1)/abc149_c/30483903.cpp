#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int x; cin >> x;

    for (;; x++) {
        bool flag = false;
        for (int i = 2; i*i <= x; i++) {
            if (x % i == 0) {
                flag = true;
                break;
            }
        }

        if (!flag) {
            cout << x << endl;
            break;
        }
    }
}
