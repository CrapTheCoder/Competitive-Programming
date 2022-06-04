#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define MAX 100005

#define endl '\n'
#define int ll

#define INF LONG_MAX

int minimum = INF;
int maximum = -INF;

int length = 0;

bool visited[MAX];
vector<int> graph[MAX];

void dfs(int u){
    if(visited[u])
        return ;

    visited[u] = true;

    minimum = min(minimum, u);
    maximum = max(maximum, u);

    length++;

    for(auto v: graph[u])
        dfs(v);
}

int dfs1(int u, int level=1){
    if(visited[u])
        return 0;

    visited[u] = true;

    int sum = level;

    for(auto v: graph[u]) {
        sum += dfs1(v, level + 1);
    }

    return sum;
}

integer main() {
    ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    int t; cin >> t;

    while(t--) {
        for(int i = 0; i < MAX; i++){
            graph[i].clear();
            visited[i] = false;
        }

        int n, m; cin >> n >> m;

        int u, v;

        for(int i = 0; i < m; i++){
            cin >> u >> v;
            u--; v--;

            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        vector<int> typeodd;
        vector<int> typeeven;

        for(int u = 0; u < n; u++){
            if(!visited[u]) {
                dfs(u);

                if(length % 2)
                    typeodd.push_back(maximum);
                else
                    typeeven.push_back(minimum);

                length = 0;

                minimum = INF;
                maximum = -INF;
            }
        }

        for(int i = 0; i < MAX; i++)
            visited[i] = false;

        int typeoddl = 0;
        int typeevenl = 0;

        for(auto u: typeodd){
            typeoddl += dfs1(u);
        }

        for(auto u: typeeven){
            typeevenl += dfs1(u);
        }

        cout << typeevenl << " " << typeoddl << endl;
    }
}