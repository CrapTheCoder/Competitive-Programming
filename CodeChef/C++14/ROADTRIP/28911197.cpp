#include <bits/stdc++.h>

using namespace std;

#define MAX 1000009

int n, m, k;

int museums[MAX] = {0};
bool visited[MAX];

int total = 0;

vector<int> graph[MAX];

int dfs(int u){
    if(visited[u])
        return 0;

    visited[u] = true;

    total += museums[u];

    for(auto v: graph[u])
        dfs(v);
}

#define endl '\n'

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
    
    int t; cin >> t;

    while(t--){
        for(int i = 0; i < MAX; i++){
            museums[i] = 0;
            visited[i] = false;
            graph[i].clear();
        }

        cin >> n >> m >> k;

        for(int i = 0; i < m; i++){
            int u, v; cin >> u >> v;

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        for(int i = 1; i <= n; i++)
            cin >> museums[i];

        vector<int> v;

        for(int i = 0; i < MAX; i++)
            visited[i] = false;

        for(int u = 1; u <= n; u++){
            if(!visited[u]){
                dfs(u);

                v.push_back(total);

                total = 0;
            }
        }

        if(v.size() < k){
            cout << -1 << endl;
            continue;
        }

        sort(v.begin(), v.end());

        int i = 0, j = v.size() - 1;

        int ans = 0;

        int l = 0;

        while(l < k){
            if(l % 2 == 0){
                ans += v[j];
                j--;
            }
            else {
                ans += v[i];
                i++;
            }
            l++;
        }

        cout << ans << endl;
    }
}
