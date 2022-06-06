#include <bits/stdc++.h>
using namespace std;
 
#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) iter.size();
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int n, m;
    cin >> n >> m;
 
    // edge
    pair<int, pair<int, int>> edges[n-1];
    for (int i = 0; i < n-1; i++) {
        cin >> edges[i].second.first >> edges[i].second.second >> edges[i].first;
        edges[i].second.first--; edges[i].second.second--;
    }
    
    sort(edges, edges+n-1);
    
    // query
    pair<int, int> queries[m];
    for (int i = 0; i < m; i++) {
        int x; cin >> x; queries[i] = {x, i};
    }
 
    sort(queries, queries + m);
 
    // process
    int answers[m];
 
    int ufds[n];
    fill(ufds, ufds+n, -1);
 
    int cur = 0, total = 0;
    for (int i = 0; i < m; i++) {
        auto [q, z] = queries[i];
 
        while (cur < n-1 && edges[cur].first <= q) {
            auto [u, v] = edges[cur].second;
            while (ufds[u] >= 0) u = ufds[u];
            while (ufds[v] >= 0) v = ufds[v];
 
            if (u != v) {
                if (-ufds[u] < -ufds[v]) swap(u, v);
 
                int v1 = -ufds[u], v2 = -ufds[v];
                total -= v1 * (v1 - 1) / 2;
                total -= v2 * (v2 - 1) / 2;
 
                ufds[u] += ufds[v];
                ufds[v] = u;
 
                v1 = -ufds[u];
                total += v1 * (v1 - 1) / 2;
            }
 
            cur++;
        }
 
        answers[z] = total;
    }
 
    // print
    for (int i = 0; i < m; i++)
        cout << answers[i] << " ";
    cout << endl;
}