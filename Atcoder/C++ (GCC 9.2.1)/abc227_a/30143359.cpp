#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, k, a;
    cin >> n >> k >> a;

    int cur_a = a;
    for (int i = 0; i < k-1; i++) {
        cur_a++;
        if (cur_a == n+1)
            cur_a = 1;
    }

    cout << cur_a << endl;
}
