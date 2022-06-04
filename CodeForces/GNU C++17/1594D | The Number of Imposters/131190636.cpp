#include <bits/stdc++.h>
#define fast ios_base::sync_with_stdio(0);cin.tie(NULL);cout.tie(NULL)
#define ll long long int
#define ld long double
using namespace std;
const int N = 1e6 + 5;
const int MOD = 1e9 + 7;
vector<pair<int, int> > graph[N];
int n, m, col[N], res, col_1[N];
bool ok = 1;
 
void dfs(int node, int p, int color){
    col[node] = color;
    if(color == 1)
        ++res;
    for(auto k : graph[node]){
        if(k.first == p) continue;
        if(!col[k.first])
            dfs(k.first, node, (k.second == 1 ? (color == 1 ? 2 : 1) : color));
        else{
            if(k.second == 1){
                if(col[k.first] == col[node]){
                    ok = 0;
                    return;
                }
            }
            else{
                if(col[k.first] != col[node]){
                    ok = 0;
                    return;
                }
            }
        }
    }
}
 
void dfs1(int node, int p, int color){
    col_1[node] = color;
    if(color == 1)
        ++res;
    for(auto k : graph[node]){
        if(k.first == p) continue;
        if(!col_1[k.first])
            dfs1(k.first, node, (k.second == 1 ? (color == 1 ? 2 : 1) :  color));
        else{
            if(k.second == 1){
                if(col_1[k.first] == col_1[node]){
                    ok = 0;
                    return;
                }
            }
            else{
                if(col_1[k.first] != col_1[node]){
                    ok = 0;
                    return;
                }
            }
        }
    }
}
 
void solve(){
    cin >> n >> m;
    ok = 1;
    for(int i = 1; i <= m; ++i){
        int type, u, v;
        string s;
 
        cin >> u >> v >> s;
 
        if (s == "imposter") type = 1;
        if (s == "crewmate") type = 2;
 
        graph[u].push_back({v, type});
        graph[v].push_back({u, type});
    }
    if(!ok){
        cout << "-1\n";
        for(int i = 1; i <= n; ++i)
            graph[i].clear();
        return;
    }
    for(int i = 1; i <= n; ++i){
        col[i] = 0;
        col_1[i] = 0;
    }
    int ans = 0;
    for(int i = 1; i <= n; ++i){
        int cur = 0, ct = 0, ct1 = 0;
        if(!col[i]){
            dfs(i, 0, 1);
            if(!ok){
                ok = 1;
                ++ct;
            }
            else
                cur = max(cur, res);
            res = 0;
        }
        if(!col_1[i]){
            dfs1(i, 0, 2);
            if(!ok){
                ok = 1;
                ++ct1;
            }
            else
                cur = max(cur, res);
            res = 0;
        }
        ans += cur;
        if(ct and ct1){
            cout << "-1\n";
            for(int i = 1; i <= n; ++i)
                graph[i].clear();
            return;
        }
    }
    cout << ans << "\n";
    for(int i = 1; i <= n; ++i)
        graph[i].clear();
}
 
int main(){
    fast;
    int t = 1;
    cin >> t;
    while(t--)
        solve();
    return 0;
}