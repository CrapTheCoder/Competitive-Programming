#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();

const int MOD = 1e9 + 7;
const int MAXX = 100000, MAXY = 500;
const int INF = LLONG_MAX >> 1;

int n;
int y[MAXX];

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    fill(y, y + MAXX, MAXY);

    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b; cin >> a >> b;
        y[a] = min(y[a], b);
    }
    
    int maxi = 0;
    for (int j = 0; j <= MAXY; j++) {
        int prev = 0;
        for (int i = 0; i <= MAXX; i++) {
            if (y[i] < j) {
                maxi = max(maxi, j * (i - prev));
                prev = i;
            }
        }

        maxi = max(maxi, j * (MAXX - prev));
    }

    cout << maxi << endl;
}
