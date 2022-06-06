bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n, q; cin >> n >> q;
int a[n];
for (int i = 0; i < n; i++)
cin >> a[i];

int ans = 0;
bool t = false;

for (int i = 0; i < n; i++) {
if (!t) {
if (i+1 == n || a[i] > a[i+1])
ans += a[i], t = !t;

} else {
if (i+1 < n && a[i] < a[i+1])
ans -= a[i], t = !t;
}


cout << ans << endl;

