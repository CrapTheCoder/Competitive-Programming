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

vector<int> b, r;

string s; cin >> s;
for (int i = 0; i < n; i++) {
if (s[i] == 'B') b.push_back(a[i]);
if (s[i] == 'R') r.push_back(a[i]);


bool flag = false;

int j = 0;

sort(b.begin(), b.end());
for (; j < b.size(); j++)
if (b[j] < j+1)
flag = true;

sort(r.begin(), r.end());
for (; j < n; j++)
if (r[j - b.size()] > j+1)
flag = true;

if (flag)
cout << "NO" << endl;
else
cout << "YES" << endl;
}
}