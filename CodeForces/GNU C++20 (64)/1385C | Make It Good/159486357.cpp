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
int n; cin >> n;

int a[n];
for (int i = 0; i < n; i++)
cin >> a[i];

int ans = n-1;
for (int i = n-1; i > 0; i--) {
if (a[i] <= a[i-1])
ans = i-1;
else
break;


for (int i = ans; i > 0; i--) {
if (a[i] >= a[i-1])
ans = i-1;
else
break;


cout << ans << endl;

