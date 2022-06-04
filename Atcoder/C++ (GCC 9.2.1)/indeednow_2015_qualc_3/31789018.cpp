#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

int n, x;
bool vis[1013][10013];
int moves[1013][2];

bool solve(int i=0, int c=0) {
    if (i == n && c == x) return true;
    if (i == n || c > x || vis[i][c]) return false;

    vis[i][c] = true;
    return solve(i+1, c+moves[i][0]) || solve(i+1, c+moves[i][1]);
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> n >> x;

    for (int i = 0; i < n; i++)
        cin >> moves[i][0] >> moves[i][1];

    cout << (solve() ? "Yes" : "No") << endl;
}
