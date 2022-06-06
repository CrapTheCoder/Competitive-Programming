bits/stdc++.h>
namespace std;

int long long
endl '\n'
all(iter) (iter).begin(), (iter).end()
rall(iter) (iter).rbegin(), (iter).rend()

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

m; cin >> n >> m;
n], b[m];
int i = 0; i < n; i++) cin >> a[i];
int i = 0; i < m; i++) cin >> b[i];

, a+n);
, b+m);

int i = 0; i < n; i++) {
for (int j = 0; j < m; j++) {
if (a[i] == b[j]) {
cout << a[i]; return 0;
}



= *min_element(a, a+n);
= *min_element(b, b+m);

> y)
swap(x, y);

<< x << y << endl;
