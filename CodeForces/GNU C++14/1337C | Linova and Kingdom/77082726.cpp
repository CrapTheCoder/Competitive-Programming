#include <bits/stdc++.h>
using namespace std;
 
#define int long long
 
#define endl '\n'
#define speed ios::sync_with_stdio(false); cin.tie(NULL);
 
#define MAXN 200010
 
int diff[MAXN];
int sizes[MAXN];
int depths[MAXN];
 
vector<int> graph[MAXN];
 
int dfs(int u=0, int p=0, int dep=0){
    dep++;
    depths[u] = dep;
 
    sizes[u] = 1;
 
    for(auto v: graph[u]){
        if(v != p)
            sizes[u] += dfs(v, u, dep);
    }
 
    diff[u] = sizes[u] - depths[u];
 
    return sizes[u];
}
 
signed main(){
    speed;
 
    int n, k; cin >> n >> k;
 
    for(int i = 0; i < n - 1; i++){
        int u, v; cin >> u >> v;
        u--; v--;
 
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
 
    dfs();
 
    sort(diff, diff + n, greater<int>());
 
    int ans = 0;
    for(int i = 0; i < n - k; i++)
        ans += diff[i];
 
    cout << ans << endl;
}