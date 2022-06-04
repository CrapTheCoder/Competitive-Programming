#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

int n, m;
char cg[1005][1005];
bool g[1005][1005];
bool visited[1005][1005];

void mark(int i, int j){
    if(i < 0 || j < 0 || i >= n || j >= m)
        return;

    if(cg[i][j] == '.')
        g[i][j] = true;
}

int c;

void dfs(int i, int j){
    if(i < 0 || j < 0 || i >= n || j >= m || !g[i][j] || visited[i][j])
        return;

    visited[i][j] = true;

    c++;

    dfs(i - 1, j - 1);
    dfs(i - 1, j);
    dfs(i - 1, j + 1);

    dfs(i, j - 1);
    dfs(i, j + 1);

    dfs(i + 1, j - 1);
    dfs(i + 1, j);
    dfs(i + 1, j + 1);
}

integer main(){
    cin >> n >> m;

    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin >> cg[i][j];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(cg[i][j] == '#'){
                mark(i - 1, j - 1);
                mark(i - 1, j);
                mark(i - 1, j + 1);

                mark(i, j - 1);
                mark(i, j + 1);

                mark(i + 1, j - 1);
                mark(i + 1, j);
                mark(i + 1, j + 1);
            }
        }
    }

    int maxi = 0;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(g[i][j]){
                c = 0;
                dfs(i, j);

                maxi = max(maxi, c);
            }
        }
    }

    cout << maxi << endl;
}
