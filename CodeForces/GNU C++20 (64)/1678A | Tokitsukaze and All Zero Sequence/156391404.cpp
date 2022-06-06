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

int zero = 0;
set<int> vals;
for (int i = 0; i < n; i++) {
int x; cin >> x;
if (x == 0)
zero++;

vals.insert(x);


(zero)
cout << n - zero << endl;

else if (vals.size() != n)
cout << n << endl;

else
cout << n + 1 << endl;

