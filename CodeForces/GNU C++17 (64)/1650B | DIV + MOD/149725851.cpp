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

int val = (r / a) * a - 1;

(val < l) {
cout << (r / a) + (r % a) << endl;

else {
cout << max((val / a) + (val % a), (r / a) + (r % a)) << endl;


