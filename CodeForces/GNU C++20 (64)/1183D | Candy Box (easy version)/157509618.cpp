bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n; cin >> n;
int a[n+1]{};
for (int i = 0; i < n; i++) {
int x; cin >> x; a[x]++;


sort(a+1, a+n+1);

int cur = INF, ans = 0;
for (int i = n; i > 0; i--) {
cur = min(cur-1, a[i]);
if (cur > 0) ans += cur;


cout << ans << endl;

