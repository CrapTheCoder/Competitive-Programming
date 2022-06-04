#include<bits/stdc++.h>
using namespace std;

#define endl '\n'
#define INF INT_MAX

int n;
int a[200005];
int pre[200005][101];
vector<vector<int>> adj;

struct LCA {
public:
    vector<int> height, euler, first, segtree;
    vector<bool> visited;

    LCA(int root) {
        height.resize(n);
        first.resize(n);
        euler.reserve(n * 2);
        visited.assign(n, false);
        dfs(adj, root);
        int m = euler.size();
        segtree.resize(m * 4);
        build(1, 0, m - 1);
    }

    void dfs(vector<vector<int>> &adj, int node, int h = 0) {
        visited[node] = true;
        height[node] = h;
        first[node] = euler.size();
        euler.push_back(node);
        for (auto to : adj[node]) {
            if (!visited[to]) {
                dfs(adj, to, h + 1);
                euler.push_back(node);
            }
        }
    }

    void build(int node, int b, int e) {
        if (b == e) {
            segtree[node] = euler[b];
        } else {
            int mid = (b + e) / 2;
            build(node << 1, b, mid);
            build(node << 1 | 1, mid + 1, e);
            int l = segtree[node << 1], r = segtree[node << 1 | 1];
            segtree[node] = (height[l] < height[r]) ? l : r;
        }
    }

    int query(int node, int b, int e, int L, int R) {
        if (b > R || e < L)
            return -1;
        if (b >= L && e <= R)
            return segtree[node];
        int mid = (b + e) >> 1;

        int left = query(node << 1, b, mid, L, R);
        int right = query(node << 1 | 1, mid + 1, e, L, R);
        if (left == -1) return right;
        if (right == -1) return left;
        return height[left] < height[right] ? left : right;
    }

    int lca(int u, int v) {
        int left = first[u], right = first[v];
        if (left > right)
            swap(left, right);
        return query(1, 0, euler.size() - 1, left, right);
    }
};

void dfs(int u=0, int p=-1){
    if(p != -1)
        for(int i = 0; i < 101; i++)
            pre[u][i] = pre[p][i];

    pre[u][a[u]]++;

    for(auto v: adj[u]){
        if(v == p)
            continue;

        dfs(v, u);
    }
}

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while(t--){
        adj.clear();
        adj.resize(200005);

        int q; cin >> n >> q;

        for(int i = 0; i < n; i++)
            cin >> a[i];

        for(int i = 0; i < n-1; i++){
            int u, v;
            cin >> u >> v;
            u--; v--;

            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        fill(pre[0], pre[0] + 101, 0);
        dfs();

        LCA f(0);

        while(q--){
            int u, v;
            cin >> u >> v;
            u--; v--;

            int w = f.lca(u, v);

            int cur[101];

            for(int i = 0; i < 101; i++)
                cur[i] = pre[u][i] + pre[v][i] - 2 * pre[w][i];

            cur[a[w]]++;

            // for(int i = 0; i < 101; i++)
            //     cout << cur[i] << " ";
            // cout << endl;

            int mini = INF;
            int last = -1;

            for(int i = 0; i < 101; i++){
                if(cur[i] > 1){
                    mini = 0;
                    break;
                }

                if(cur[i] == 1){
                    if(last != -1)
                        mini = min(mini, i - last);

                    last = i;
                }
            }

            cout << mini << endl;
        }
    }
}
