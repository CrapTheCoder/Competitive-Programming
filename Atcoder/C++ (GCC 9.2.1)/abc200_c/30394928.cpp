#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    map<int, int> count;
    for (int i = 0; i < n; i++) {
        int x; cin >> x;
        count[x]++;
    }

    int answer = 0;
    for (int i = 0; i < 200; i++) {
        int total = 0;
        for (auto [x, y] : count)
            if ((x - i) % 200 == 0)
                total += y;

        answer += total * (total - 1) / 2;
    }

    cout << answer << endl;
}
