#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
 
int n;
bool done;
int children[100013];
vector<int> g[100013];
 
int dfs(int u=0, int p=-1) {
    for (auto v: g[u])
        if (v != p)
            children[u] += dfs(v, u);
 
    if (!done and children[u] * 2 == n) {
        done = true;
        int mid = g[p][0] != u ? g[p][0] : g[p][1];
 
        cout << p+1 << " " << mid+1 << endl;
        cout << u+1 << " " << mid+1 << endl;
    }
 
    return children[u];
}
 
int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
 
 int t; cin >> t;
 
 while (t--) {
        cin >> n;
 
        done = false;
        for (int i = 0; i <= n; i++) {
            children[i] = 1;
            g[i].clear();
        }
 
        for (int i = 0; i < n-1; i++) {
            int u, v;
            cin >> u >> v;
            u--; v--;
 
            g[u].push_back(v);
            g[v].push_back(u);
        }
 
        dfs();
 
        if (!done) {
            cout << 1 << " " << g[0][0]+1 << endl;
            cout << 1 << " " << g[0][0]+1 << endl;
        }
 }
}