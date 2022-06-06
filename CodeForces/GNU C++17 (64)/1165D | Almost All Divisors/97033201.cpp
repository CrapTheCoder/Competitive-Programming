#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int t; cin >> t;

while (t--) {
int n; cin >> n;
int a[n];
set<int> f;

for (int i = 0; i < n; i++) {
cin >> a[i];
f.insert(a[i]);
}

sort(a, a+n);

int d = a[0] * a[n-1];

set<int> ns;

for (int i = 2; i*i <= d; i++) {
if (d % i == 0) {
ns.insert(i);
ns.insert(d/i);
}
}

if (ns != f) {
cout << -1 << endl;
continue;
}

cout << d << endl;
}
}