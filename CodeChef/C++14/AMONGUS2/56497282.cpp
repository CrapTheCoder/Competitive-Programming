#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

long long get_rand() {
    long long a = rand();
    long long b = rand();
    return a * (RAND_MAX + 1ll) + b;
}

#define int long long
//#define ordered_set tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update>
//#define ordered_multiset tree<int, null_type, less_equal<int>, rb_tree_tag, tree_order_statistics_node_update>

const int intmin = -100000000000000000LL;
const int intmax = 100000000000000000LL;

vector<pair<int, int>> adj[500001]; //node, type of edge
vector<int> visited(500001, 0), color(500001, 0);

int one = 0, siz = 0;
bool dfs(int node, int col){
    siz++;
    visited[node] = 1;
    color[node] = col;
    if(col == 0){
        one++;
    }

    for (pair<int, int> child : adj[node])
    {
        if(visited[child.first] == 0){
            if(child.second == 0){
                if (!dfs(child.first, !col))
                    return false;
            }
            else{
                if (!dfs(child.first, col))
                    return false;
            }
        }
        else{
            if(child.second == 0 && color[child.first] == col){
                return false;
            }
            else if(child.second == 1 && color[child.first] != col){
                return false;
            }
        }
    }

    return true;
}

int32_t main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    int T;
    cin >> T;
    while(T--){
        one = 0;
        siz = 0;

        int n, q;
        cin >> n >> q;

        //edge types: 1 for same team, 0 for different team
        for (int i = 0; i < q; ++i)
        {
            int type, a, b;
            cin >> type >> a >> b;
            type--;

            adj[a].push_back({b, type});
            adj[b].push_back({a, type});
        }

        bool done = false;
        int ans = 0;
        for (int i = 1; i <= n; ++i)
        {
            if(visited[i] == 0){
                if(!dfs(i, 0)){
                    done = true;
                    break;
                }
                else{
                    ans += max(one, siz-one);
                    one = 0;
                    siz = 0;
                }
            }
        }

        if(done){
            cout << "-1\n";
        }
        else{
            cout << ans << '\n';
        }

        for (int i = 0; i <= n; ++i)
        {
            adj[i].clear();
            color[i] = 0;
            visited[i] = 0;
        }
    }
}