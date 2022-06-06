#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
 
const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int W, H;
        cin >> W >> H;
 
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
 
        int r = x2 - x1, c = y2 - y1;
 
        int w, h;
        cin >> w >> h;
 
        int ans = INF;
 
        if (w + r <= W) {
            ans = min(ans, max(0LL, w - x1));
            ans = min(ans, max(0LL, x2 - (W - w)));
        }
 
        if (h + c <= H) {
            ans = min(ans, max(0LL, h - y1));
            ans = min(ans, max(0LL, y2 - (H - h)));
        }
 
        if (ans == INF)
            cout << -1 << endl;
        else
            cout << ans << endl;
    }
}