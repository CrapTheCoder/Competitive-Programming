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
int x, y, k;
cin >> x >> y >> k;

int cs = k*y + k - 1;
int ds = x-1;

cout << (cs + ds - 1) / ds + k << endl;

