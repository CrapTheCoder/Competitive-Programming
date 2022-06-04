#include <bits/stdc++.h>
using namespace std;
vector<int> v[100005];
int LN = 18;
int father[19][100005];
int depth[100005];

void dfs(int current, int parent){
    father[0][current] = parent;
    depth[current] = depth[parent] + 1;
    for(int node: v[current]){
        if(node!=parent)
            dfs(node, current);
    }
}

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n, q;
    cin >> n >> q;

    for(int i=1; i<n; i++){
        int x, y; cin >> x >> y;
        x--; y--;

        v[x].push_back(y);
        v[y].push_back(x);
    }

    depth[0] = -1;
    dfs(0, -1);

    for(int j=1; j<=LN; j++)
        for(int i=1; i<=n; i++)
            father[j][i] = father[j-1][father[j-1][i]];

    while(q--){
        int x, y; cin >> x >> y;
        x--;

        int ans;

        if(y>=depth[x])
            ans = -1;
        else
        {
            int diff = y;
            ans = x;
            for(int i=0; i<LN; i++){
                if(diff & (1<<i)){
                    ans = father[i][ans];
                }
            }

            ans++;
        }
        cout << ans << "\n";
    }
    return 0;
}
