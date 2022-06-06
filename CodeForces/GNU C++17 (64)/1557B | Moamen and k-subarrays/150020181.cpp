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
int n, k; cin >> n >> k;

pair<int, int> a[n];
for (int i = 0; i < n; i++)
cin >> a[i].first, a[i].second = i;

sort(a, a+n);

int count = 1;
for (int i = 1; i < n; i++)
if (a[i-1].second + 1 != a[i].second)
count++;

cout << (count <= k ? "YES" : "NO") << endl;

