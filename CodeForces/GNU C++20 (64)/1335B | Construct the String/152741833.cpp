bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

string alps = "abcdefghijklmnopqrstuvwxyz";

main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int n, a, b;
cin >> n >> a >> b;

string res;
for (int i = 0; i < n; i++)
res += alps[i%b];

cout << res << endl;

