#include <bits/stdc++.h>
using namespace std;

bool BFS(vector<int> adj[], int src, int dest, int v, int dist[])
{
	list<int> queue;

	bool visited[v];

	for (int i = 0; i < v; i++) {
		visited[i] = false;
		dist[i] = INT_MAX;
	}

	visited[src] = true;
	dist[src] = 0;
	queue.push_back(src);

	while (!queue.empty()) {
		int u = queue.front();
		queue.pop_front();
		for (int i = 0; i < adj[u].size(); i++) {
			if (visited[adj[u][i]] == false) {
				visited[adj[u][i]] = true;
				dist[adj[u][i]] = dist[u] + 1;
				queue.push_back(adj[u][i]);

				if (adj[u][i] == dest)
				return true;
			}
		}
	}

	return false;
}

int solve(vector<int> adj[], int s, int dest, int v)
{
	int dist[v];
	bool x = BFS(adj, s, dest, v, dist);

	if(x == true) return dist[dest];
    else return 0;
}

int main()
{
	int n, m;  cin >> n >> m;
	vector<int> adj[n];

	for(int i = 0; i < m; i++){
        int u, v; cin >> u >> v;
        u -= 1; v -= 1;

        adj[u].push_back(v);
        adj[v].push_back(u);
	}

	int s, d; cin >> s >> d;
	s -= 1; d -= 1;

	cout << solve(adj, s, d, n);
}

