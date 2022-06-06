#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int tc; cin >> tc;
while (tc--) {
int n; cin >> n;

int a[n];
for (int i = 0; i < n; i++)
cin >> a[i];

sort(a, a+n);

int c0 = 0, c1 = 0;
for (auto i : a) {
if (c0 == i)
c0++;
else if (c1 == i)
c1++;
}

cout << c0 + c1 << endl;
}
}