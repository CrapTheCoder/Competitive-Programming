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

(n % 2) {
cout << "NO" << endl;
continue;


sort(a, a+n);

vector<int> b;
for (int i = 0, j = n/2; j < n; i++, j++) {
b.push_back(a[i]);
b.push_back(a[j]);


bool flag = true;
for (int i = 0; i < n; i++) {
flag = flag && ((b[(i-1+n) % n] < b[i] && b[i] > b[(i+1) % n])
|| (b[(i-1+n) % n] > b[i] && b[i] < b[(i+1) % n]));


if (flag) {
cout << "YES" << endl;
for (auto i : b)
cout << i << " ";
cout << endl;

} else {
cout << "NO" << endl;
}
}
}