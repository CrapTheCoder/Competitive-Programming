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
int n, m;
cin >> n >> m;

bool a[n][m];
for (int i = 0; i < n; i++) {
for (int j = 0; j < m; j++) {
char x; cin >> x;
a[i][j] = (x == '1');
}


for (int i = 0; i < n-1; i++) {
for (int j = 0; j < m-1; j++) {
int c = a[i][j] + a[i+1][j] + a[i][j+1] + a[i+1][j+1];

if (c == 3) {
cout << "NO" << endl;
goto breaker;
}
}


cout << "YES" << endl;
breaker: ;

}