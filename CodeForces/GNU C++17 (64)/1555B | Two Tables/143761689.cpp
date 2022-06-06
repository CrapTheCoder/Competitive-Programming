bits/stdc++.h>
namespace std;

int long long
endl '\n'
all(iter) (iter).begin(), (iter).end()
rall(iter) (iter).rbegin(), (iter).rend()

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int W, H;
cin >> W >> H;

int x1, y1, x2, y2;
cin >> x1 >> y1 >> x2 >> y2;

int r = x2 - x1, c = y2 - y1;

int w, h;
cin >> w >> h;

int ans = INF;

(w + r <= W) {
ans = min(ans, max(0LL, w - x1));
ans = min(ans, max(0LL, x2 - (W - w)));


(h + c <= H) {
ans = min(ans, max(0LL, h - y1));
ans = min(ans, max(0LL, y2 - (H - h)));


if (ans == INF)
cout << -1 << endl;
else
cout << ans << endl;
}
}