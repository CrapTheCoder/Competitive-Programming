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
int c = 0;

while (n % 3 == 0 && n % 2 == 0)
n /= 6, c++;

while (n % 3 == 0)
n /= 3, c += 2;

(n == 1)
cout << c << endl;
else
cout << -1 << endl;

