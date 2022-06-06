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
int n, a, b, c, d;
cin >> n >> a >> b >> c >> d;

(n * (a - b) <= (c + d) && n * (a + b) >= (c - d))
cout << "YES" << endl;
else
cout << "NO" << endl;

