bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

m, q;
n >> m >> q;

<int> a(n*m);
int x = 0; x < n; x++) {
for (int y = 0; y < m; y++) {
char c; cin >> c;
a[x + y*n] = (c == '*');



= accumulate(a.begin(), a.end(), 0);
= accumulate(a.begin() + t, a.end(), 0);

(q--) {
int x, y; cin >> x >> y;
--; y--;

int k = x + y*n;
k] ^= 1;

(k < t) (a[k] == 1) ? c-- : c++;
(a[k] == 1 && a[t++] == 0) c++;
(a[k] == 0 && a[--t] == 0) c--;

cout << c << endl;

}