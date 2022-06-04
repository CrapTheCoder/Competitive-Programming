#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

int n, k;
set<int> a[300];

bool visited[300];

void dfs(int u){
    visited[u] = true;

    for(int v = 0; v < n; v++){
        if(!visited[v]){
            int common = 0;

            for(auto j: a[v]){
                if(a[u].find(j) != a[u].end())
                    common++;
            }

            if(common >= k){
                dfs(v);
            }
        }
    }
}

int main(){
    cin >> n >> k;

    for(int i = 0; i < n; i++)
        visited[i] = false;

    int l;

    for(int i = 0; i < n; i++){
        cin >> l;

        for(int j = 0; j < l; j++){
            int v; cin >> v;
            a[i].insert(v);
        }
    }

    dfs(0);

    int cnt = 0;

    for(int i = 0; i < n; i++){
        if(visited[i])
            cnt++;
    }

    cout << cnt << '\n';
}
