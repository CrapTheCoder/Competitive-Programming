bits/stdc++.h>
namespace std;

endl '\n'
int long long

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

int n) {
int c = 2; c*c <= n; c++)
(n % c == 0)
return false;

(n >= 2);


main() {
sync_with_stdio(false); cin.tie(NULL);

; cin >> tc;
(tc--) {
int d; cin >> d;

int p, q;
for (p = d+1; ; p++)
if (pc(p))
break;

for (q = d+p; ; q++)
if (pc(q))
break;

cout << p*q << endl;

