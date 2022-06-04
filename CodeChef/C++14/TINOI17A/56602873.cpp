#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int hasher(int x, int y) {
    return x * MOD + y;
}

int r, c, n;
unordered_set<int> s;
unordered_multimap<int, int> pat;
unordered_map<int, bool> vis;
unordered_map<int, bool> vis2;
unordered_map<int, vector<int>> graph;

int val = 0;
void dfs(int u) {
    if (vis[u]) return;
    vis[u] = true;
    
    int x = u / MOD, y = u % MOD;
    pat.insert({hasher(x-1, y), 0});
    pat.insert({hasher(x+1, y), 1});
    pat.insert({hasher(x, y-1), 2});
    pat.insert({hasher(x, y+1), 3});

    for (auto v : graph[u])
        dfs(v);
}

void dfs2(int u) {
    if (vis2[u]) return;
    vis2[u] = true;

    pat.erase(u);
    for (auto v : graph[u])
        dfs2(v);
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    cin >> r >> c >> n;
    for (int i = 0; i < n; i++) {
        int x, y;
        cin >> x >> y;

        int cur = hasher(x, y);

        if (s.count(hasher(x-1, y)) != 0) graph[cur].push_back(hasher(x-1, y)), graph[hasher(x-1, y)].push_back(cur);
        if (s.count(hasher(x+1, y)) != 0) graph[cur].push_back(hasher(x+1, y)), graph[hasher(x+1, y)].push_back(cur);
        if (s.count(hasher(x, y-1)) != 0) graph[cur].push_back(hasher(x, y-1)), graph[hasher(x, y-1)].push_back(cur);
        if (s.count(hasher(x, y+1)) != 0) graph[cur].push_back(hasher(x, y+1)), graph[hasher(x, y+1)].push_back(cur);
        s.insert(cur);
    }

    int maxi = 0;
    for (auto i : s) {
        if (!vis[i]) {
            pat.clear(); dfs(i); dfs2(i);
            maxi = max(maxi, (int) pat.size());
        }
    }
    
    cout << maxi << endl;
}
