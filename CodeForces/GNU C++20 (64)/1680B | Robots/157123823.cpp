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
int n, m;
cin >> n >> m;

int mi = INF, mj = INF;

string a[n];
for (int i = 0; i < n; i++) {
cin >> a[i];
for (int j = 0; j < m; j++)
if (a[i][j] == 'R')
mi = min(mi, i), mj = min(mj, j);


cout << (a[mi][mj] == 'R' ? "YES" : "NO") << endl;

