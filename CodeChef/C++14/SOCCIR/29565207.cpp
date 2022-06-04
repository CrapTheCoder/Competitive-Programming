#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

int cnt = 0;

vector<int> graph[100005];
bool visited[100005];

void dfs(int u){
    if(visited[u])
        return;

    visited[u] = true;
    cnt++;

    for(auto v: graph[u])
        dfs(v);
}

integer main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m; cin >> n >> m;
    int u, v;

    while(m--){
        cin >> u >> v;
        u--; v--;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> ans;

    for(int u = 0; u < n; u++){
        if(!visited[u]){
            dfs(u);
            ans.push_back(cnt);

            cnt = 0;
        }
    }

    sort(ans.begin(), ans.end());

    cout << ans.size() << endl;

    for(auto c: ans)
        cout << c << " ";

    cout << endl;
}
