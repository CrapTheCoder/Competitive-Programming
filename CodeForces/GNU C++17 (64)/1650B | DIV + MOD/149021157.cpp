bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

a, int x) {
x / a + x % a;


main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;

(tc--) {
int l, r, a;
cin >> l >> r >> a;

int x = r - r%a - 1;

(l <= x)
cout << max(f(a, r), f(a, x)) << endl;
else
cout << f(a, r) << endl;

