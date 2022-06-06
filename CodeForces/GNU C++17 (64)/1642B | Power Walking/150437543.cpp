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
int n; cin >> n;

set<int> a;
for (int i = 0; i < n; i++) {
int x; cin >> x;
a.insert(x);


for (int k = 1; k <= n; k++)
cout << max((int)a.size(), k) << " ";
cout << endl;

