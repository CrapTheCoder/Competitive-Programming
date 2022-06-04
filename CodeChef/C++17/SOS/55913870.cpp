#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()
#define size_of(iter) (int) (iter).size();

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

int n;
string s;
vector<int> tree[200013];

bool vis[200013];

int cnt;
void dfs(int u) {
    if (vis[u])
        return;
    
    vis[u] = true;

    if (s[u] == 'B')
        cnt++;
    
    for (auto v : tree[u])
        dfs(v);
}

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        cin >> n >> s;
        for (int i = 0; i < n; i++) {
            tree[i].clear(); vis[i] = false;
        }
        
        for (int i = 0; i < n-1; i++) {
            int u, v; cin >> u >> v;
            u--; v--;

            if ((s[u] == 'R' && s[v] == 'G') || (s[u] == 'G' && s[v] == 'R'))
                continue;
            
            tree[u].push_back(v);
            tree[v].push_back(u);
        }

        bool flag = false;
        for (int u = 0; u < n; u++) {
            if (!vis[u]) {
                cnt = 0;
                dfs(u);

                if (cnt > 1)
                    flag = true;
            }
        }

        if (flag)
            cout << "No" << endl;
        else
            cout << "Yes" << endl;
    }
}
