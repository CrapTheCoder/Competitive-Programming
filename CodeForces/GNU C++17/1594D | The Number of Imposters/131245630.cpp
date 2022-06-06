#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
 
signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);
 
    int tc; cin >> tc;
    while (tc--) {
        int n, m; cin >> n >> m;
        vector<pair<int, int>> graph[n];
 
        for (int _ = 0; _ < m; _++) {
            int i, j; string c;
            cin >> i >> j >> c;
            i--; j--;
 
            if (c[0] == 'c') {
                graph[i].push_back({j, 0});
                graph[j].push_back({i, 0});
 
            } else {
                graph[i].push_back({j, 1});
                graph[j].push_back({i, 1});
            }
        }
 
        int cl[n];
        bool vis[n] = {false};
 
        fill(cl, cl + n, -1);
 
        function<int(int)> color = [&](int u) {
            vis[u] = true;
 
            int par = 0;
            if (cl[u] == 1)
                par++;
 
            for (auto g : graph[u]) {
                int v = g.first, w = g.second;
 
                if (w == 0) {
                    if (cl[v] == -1) {
                        cl[v] = cl[u];
 
                        int sol = color(v);
                        if (sol == -1) return sol;
 
                        par += sol;
 
                    } else if (cl[v] != cl[u])
                        return -1;
 
                } else {
                    if (cl[v] == -1) {
                        cl[v] = cl[u] ^ 1;
 
                        int sol = color(v);
                        if (sol == -1) return sol;
 
                        par += sol;
 
                    } else if (cl[v] == cl[u])
                        return -1;
                }
            }
 
            return par;
        };
 
        function<void(int)> clr = [&](int u) {
            if (cl[u] != -1) {
                cl[u] = -1;
                for (auto v : graph[u])
                    clr(v.first);
            }
        };
 
        bool flag = false;
        int maxi = 0;
 
        for (int u = 0; u < n; u++) {
            if (!vis[u]) {
                cl[u] = 0;
                int s1 = color(u);
                clr(u);
 
                cl[u] = 1;
                int s2 = color(u);
                clr(u);
 
                if (s1 == s2 && s2 == -1) {
                    cout << -1 << endl;
                    flag = true;
                    break;
                }
 
                maxi += max(s1, s2);
            }
        }
 
        if (!flag)
            cout << maxi << endl;
    }
}