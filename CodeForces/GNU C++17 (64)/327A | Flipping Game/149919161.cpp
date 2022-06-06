bits/stdc++.h>
namespace std;

int long long
endl '\n'

MOD = 1e9 + 7;
INF = LLONG_MAX >> 1;

main() {
sync_with_stdio(false); cin.tie(NULL);

cin >> n;
n];
int i = 0; i < n; i++)
cin >> a[i];

oc = count(a, a+n, 1);

oc == n) {
cout << oc - 1 << endl;
return 0;


gain[n];
int i = 0; i < n; i++) {
(a[i] == 0) gain[i] = 1;
(a[i] == 1) gain[i] = -1;


= 0, mc = 0;
int i = 0; i < n; i++) {
+= gain[i];
(s < 0)
s = 0;

mc = max(mc, s);


cout << oc + mc << endl;
}