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
int n, k; cin >> n >> k;

int s = 0; pair<int, int> a[n];
for (int i = 0; i < n; i++) {
cin >> a[i].first; s += a[i].first;
a[i] = {-a[i].first + (n-i-1), i};


sort(a, a+n);
for (int i = 0; i < k; i++)
s += a[i].first;

cout << s - k * (k-1) / 2 << endl;

