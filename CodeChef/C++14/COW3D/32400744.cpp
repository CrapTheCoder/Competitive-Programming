#include "bits/stdc++.h"
using namespace std;

#define MAXN 300000
#define level 22

vector <int> tree[MAXN];
int depth[MAXN];
int parent[MAXN][level];

// pre-compute the depth for each node and their
// first parent(2^0th parent)
// time complexity : O(n)
void dfs(int cur, int prev)
{
    depth[cur] = depth[prev] + 1;
    parent[cur][0] = prev;
    for (int i=0; i<tree[cur].size(); i++)
    {
        if (tree[cur][i] != prev)
            dfs(tree[cur][i], cur);
    }
}

// Dynamic Programming Sparse Matrix Approach
// populating 2^i parent for each node
// Time complexity : O(nlogn)
void precomputeSparseMatrix(int n)
{
    for (int i=1; i<level; i++)
    {
        for (int node = 1; node <= n; node++)
        {
            if (parent[node][i-1] != -1)
                parent[node][i] =
                    parent[parent[node][i-1]][i-1];
        }
    }
}

// Returning the LCA of u and v
// Time complexity : O(log n)
int lca(int u, int v)
{
    if (depth[v] < depth[u])
        swap(u, v);

    int diff = depth[v] - depth[u];

    // Step 1 of the pseudocode
    for (int i=0; i<level; i++)
        if ((diff>>i)&1)
            v = parent[v][i];

    // now depth[u] == depth[v]
    if (u == v)
        return u;

    // Step 2 of the pseudocode
    for (int i=level-1; i>=0; i--)
        if (parent[u][i] != parent[v][i])
        {
            u = parent[u][i];
            v = parent[v][i];
        }

    return parent[u][0];
}

void addEdge(int u,int v)
{
    tree[u].push_back(v);
    tree[v].push_back(u);
}

signed main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    memset(parent,-1,sizeof(parent));

    int n, q; cin >> n >> q;

    for(int i = 0; i < n - 1; i++){
        int asd1, asd2; cin >> asd1 >> asd2;

        addEdge(asd1, asd2);
    }

    depth[0] = 0;

    // running dfs and precalculating depth
    // of each node.
    dfs(1,0);

    // Precomputing the 2^i th ancestor for evey node
    precomputeSparseMatrix(n);

    while(q--){
        int k; cin >> k;

        int asd[k];
        cin >> asd[0];

        int cur = asd[0];

        for(int i = 1; i < k; i++){
            cin >> asd[i];
            cur = lca(cur, asd[i]);
        }

        bool flag = false;

        for(int i = 0; i < k; i++){
            if(cur == asd[i]){
                cout << cur << "\n";
                flag = true;
                break;
            }
        }

        if(!flag)
            cout << -1 << "\n";
    }
}
