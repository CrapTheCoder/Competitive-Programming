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
int l, r, a;
cin >> l >> r >> a;

int v = r - r%a - 1;

(v >= l)
cout << max(r / a + r % a, v / a + v % a) << endl;
else
cout << r / a + r % a << endl;

