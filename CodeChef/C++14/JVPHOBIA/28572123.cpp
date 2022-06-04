#include <bits/stdc++.h>
using namespace std;

#define endl '\n'

typedef long long int ll;

int n, m, s;
int k;
vector<pair<int, int>> gr[100000];

bool visited[100000];

void dfs(int u){
    if(visited[u])
        return;

    visited[u] = true;

    for(auto v: gr[u]){
        if(v.second <= s)
            dfs(v.first);
    }
}

int main(){
    memset(visited, sizeof(visited), false);
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, m; cin >> n >> m;

    for(int i = 0; i < m; i++){
        int u, v, s; cin >> u >> v >> s;

        u--;
        v--;

        gr[u].push_back(make_pair(v, s));
        gr[v].push_back(make_pair(u, s));
    }

    cin >> k >> s;

    int c = 0;

    for(int i = 0; i < k; i++){
        int d; cin >> d;

        dfs(d - 1);
    }

    for(int i = 0; i < n; i++){
        if(visited[i])
            c++;
    }

    cout << c << endl;
}
