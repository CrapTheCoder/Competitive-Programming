bits/stdc++.h>
namespace std;

main() {
; cin >> tc;
(tc--) {
int l, r, a;
cin >> l >> r >> a;

int val = (r / a) * a - 1;

(val < l) {
cout << (r / a) + (r % a) << endl;

else {
cout << max((val / a) + (val % a), (r / a) + (r % a)) << endl;


