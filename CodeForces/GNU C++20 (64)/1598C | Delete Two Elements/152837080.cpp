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
int a[n]; double s = 0;
for (int i = 0; i < n; i++)
cin >> a[i], s += a[i];

/= n;

int ans = 0;
map<double, int> p;

for (auto i : a)
ans += p[2*s - i], p[i]++;

cout << ans << endl;


