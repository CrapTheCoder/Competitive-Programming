#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll

int n, m, k, a, b;

int graph[10001][10001];

int dijkstra(){
    int dist[n];
    bool visited[n];

    for(int i = 0; i < n; i++){
        dist[i] = LONG_MAX;
        visited[i] = false;
    }

    priority_queue<pair<int, int>> q;

    dist[a] = 0;

    q.push({0, a});

    while(!q.empty()){
        int u = q.top().second;

        q.pop();

        if(visited[u])
            continue;

        visited[u] = true;

        for(int v = 0; v < n; v++){
            if(graph[u][v] == 0)
                continue;

            if(dist[u] + graph[u][v] < dist[v]){
                dist[v] = dist[u] + graph[u][v];

                q.push({-dist[v], v});
            }
        }
    }

    return dist[b];
}

integer main()
{
    int t; cin >> t;

    while(t--){
        cin >> n >> m >> k >> a >> b;

        a--; b--;

        for(int i = 0; i < m; i++){
            int u, v, w; cin >> u >> v >> w;
            u--; v--;

            graph[u][v] = w;
        }

        int mini = LONG_MAX;

        for(int i = 0; i < k; i++){
            int u, v, w; cin >> u >> v >> w;
            u--; v--;

            graph[u][v] = w;
            graph[v][u] = w;

            mini = min(mini, dijkstra());

            graph[u][v] = 0;
            graph[v][u] = 0;
        }
        
        if(mini == LONG_MAX)
            cout << -1 << endl;
        else
            cout << mini << endl;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                graph[i][j] = 0;
            }
        }
    }
}
