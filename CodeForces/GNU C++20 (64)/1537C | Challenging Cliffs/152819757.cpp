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

int a[n];
for (int i = 0; i < n; i++)
cin >> a[i];

sort(a, a+n);

(n == 2) {
cout << a[0] << " " << a[1] << endl;
continue;


int mini = INF, pos = -1;
for (int i = 1; i < n; i++) {
if (a[i] - a[i-1] < mini) {
mini = a[i] - a[i-1];
pos = i;
}


for (int i = pos; i < n; i++)
cout << a[i] << " ";

for (int i = 0; i < pos; i++)
cout << a[i] << " ";

cout << endl;
}
}