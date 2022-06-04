#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, x;
    cin >> n >> x;

    x--;

    int a[n];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        a[i]--;
    }

    bool visited[n];
    fill(visited, visited+n, false);

    int count = 0;
    while (!visited[x]) {
        visited[x] = true;
        count++;

        x = a[x];
    }

    cout << count << endl;
}
