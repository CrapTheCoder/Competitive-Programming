#include <bits/stdc++.h>
    using namespace std;
    typedef unsigned long long int ll;
    #define fastio ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    #define INF 0x3f3f3f3f3f

    vector<bool> processed(3600);
    vector<ll> dist(3600);
    priority_queue<pair<ll,ll>> q;
    ll n,m,s,t,a,b;
    vector<pair<ll,ll>> adj[3600];

    void dijkstra(ll s){

        for(ll i = 0; i < n; i++) {
            dist[i] = INF;
            processed[i] = false;
        }
        dist[s] = 0;
        q.push({0,s});

        while(!q.empty()){
            ll a = q.top().second;
            q.pop();
            if(processed[a] == true) continue;
            processed[a] = true;
            for(auto u : adj[a]){
                ll b = u.first;
                ll w = u.second;
                if(dist[a]+w < dist[b]){
                    dist[b] = dist[a]+w;
                    q.push({-dist[b] , b});
                }
            }
        }

    }

    int main() {

        fastio;

        try {


            cin >> n >> m;
            for (ll i = 0; i < m; i++) {
                cin >> a >> b;
                adj[a - 1].push_back(make_pair(b - 1, 1));
                adj[b - 1].push_back(make_pair(a - 1, 1));
            }
            cin >> s >> t;

            dijkstra(s - 1);

            if (dist[t - 1] == INF) cout << "0";
            else cout << dist[t - 1];
        }

        catch (...) {
            cout << 0;
        }

        return 0;
    }