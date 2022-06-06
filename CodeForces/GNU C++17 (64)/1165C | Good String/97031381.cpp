#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

signed main() {
int n; cin >> n;
char a[n]; cin >> a;

int c = 0;
string ns;

for (int i = 0; i+1 < n; i++) {
if (a[i] == a[i+1]) {
c++;

} else {
ns += a[i];
ns += a[i+1];
i++;
}
}

if (ns.size() % 2 == 1) {
cout << n - ns.size() + 1 << endl;
for (int i = 0; i < ns.size() - 1; i++)
cout << ns[i];

} else {
cout << n - ns.size() << endl;
cout << ns << endl;
}
}