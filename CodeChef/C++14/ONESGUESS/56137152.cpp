#include <bits/stdc++.h>
using namespace std;

#define int long long
// #define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    // ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    int c = 1;
    for (int i = 0; i < n; i++) {
        cout << c << endl;
        int x; cin >> x;
        if (x == 1) c++;
    }
}
