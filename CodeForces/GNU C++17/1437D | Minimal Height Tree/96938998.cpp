#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long
#define INF INT_MAX

int n;
int a[200013];
vector<int> g[200013];

int dfs(int u=0, int p=-1, int d=0) {
int m = d;
for (auto v : g[u])
if (v != p)
m = max(m, dfs(v, u, d+1));

return m;
}

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

int t; cin >> t;

while (t--) {
int n; cin >> n;

int a[n];
for (int i = 0; i < n; i++) {
cin >> a[i]; a[i]--;
}

int c = 0;
for (int i = 1; i < n; i++) {
int s = g[a[c]].size();
if ((s > 0) && (g[a[c]][s-1] > a[i]))
c++;

g[a[c]].push_back(a[i]);
}

cout << dfs() << endl;

for (int i = 0; i < n; i++)
g[i].clear();
}
}