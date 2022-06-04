#include <bits/stdc++.h>
using namespace std;

typedef int integer;
typedef long long int ll;

#define INF LLONG_MAX

#define int ll
#define endl '\n'

integer main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

	string graph[1001];
	int t; cin >> t;

	while(t--){
		int n, k; cin >> n >> k;

		for(int i = 0; i < n; i++)
			cin >> graph[i];

		queue<int> q; q.push(0);

		bool visited[n] = {0};
		int dist[n]; fill(dist, dist + n, INF);

		visited[0] = true;
		dist[0] = 0;

		while(!q.empty()){
			int u = q.front(); q.pop();

			for(int v = max(0LL, u - k); v <= min(n - 1, u + k); v++){
				if(graph[u][v] == '1' && u != v)
				{
					if(!visited[v]){
						q.push(v);
						visited[v] = true;
					}

					if(dist[v] > dist[u]+1)
						dist[v] = dist[u] + 1;
				}
			}

		}

		if(dist[n-1] != INF)
			cout << dist[n-1] << endl;
		else
			cout << -1 << endl;
	}
}
