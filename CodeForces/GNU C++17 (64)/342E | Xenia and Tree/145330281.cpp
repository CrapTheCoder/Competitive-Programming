bits/stdc++.h>
namespace std;

int long long
endl '\n'

INF = LLONG_MAX >> 1;
LOG = 20;
BLOCK = 300;


100013];
<int> reds;
<int> tree[100013];

() {
vis[n]; memset(vis, false, sizeof vis);
pair<int, int>> q;

auto u : reds)
push({u, 0});

(!q.empty()) {
auto [u, w] = q.front(); q.pop();

(!vis[u]) {
vis[u] = true, md[u] = min(md[u], w);
for (auto v : tree[u])
q.push({v, w+1});




100013];
100013][LOG];

int u=0, int p=0, int d=0) {
][0] = p; dep[u] = d;
int j = 1; j < LOG; j++)
par[u][j] = par[par[u][j-1]][j-1];

for (auto v : tree[u])
if (v != p)
dfs(v, u, d+1);
}

int dist(int u, int v) {
int ans = 0;
if (dep[u] < dep[v])
swap(u, v);

int k = dep[u] - dep[v];

for (int i = 0; i < LOG; i++) {
if ((k >> i) & 1) {
u = par[u][i];
ans += 1 << i;
}
}

if (u == v)
return ans;

for (int i = LOG - 1; i >= 0; i--) {
if (par[u][i] != par[v][i]) {
u = par[u][i], v = par[v][i];
ans += 2 * (1 << i);
}
}

return ans+2;
}

signed main() {
ios::sync_with_stdio(false); cin.tie(NULL);

cin >> n >> m;

for (int i = 0; i < n-1; i++) {
int u, v; cin >> u >> v;
u--; v--;

tree[u].push_back(v);
tree[v].push_back(u);
}

dfs();
reds.push_back(0);
fill(md, md+n, INF);

while (m--) {
int t, v;
cin >> t >> v; v--;

if (t == 1) {
reds.push_back(v);
if (reds.size() >= BLOCK)
count(), reds.clear();

} else {
int mini = md[v];
for (auto u : reds)
mini = min(mini, dist(u, v));

cout << mini << endl;
}
}
}