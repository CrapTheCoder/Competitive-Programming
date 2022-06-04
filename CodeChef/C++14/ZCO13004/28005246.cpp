#include <bits/stdc++.h>

using namespace std;

int main(){
    int n, m, k; cin >> n >> m >> k;
    int ls[n][m];

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++)
            ls[i][j] = 1;
    }

    for(int i = 0; i < k; i++){
        int r, c, s, f; cin >> r >> c >> s >> f;
        r--; c--;

        ls[r][c] = 0;

        for(int i = 0; i < n; i++){
            int x = (i + c) - (s + abs(i - r));

            if(x >= 0 && x % f == 0)
                ls[i][c] = 0;
        }

        for(int j = 0; j < m; j++){
            int x = (r + j) - (s + abs(j - c));

            if(x >= 0 && x % f == 0)
                ls[r][j] = 0;
        }
    }

    if(ls[n-1][m-1] == 0 || ls[0][0] == 0){
        cout << "NO" << endl;
    }

    else {
        for(int i = 1; i < n; i++)
            ls[i][0] = ls[i - 1][0];

        for(int j = 1; j < m; j++)
            ls[0][j] = ls[0][j - 1];

        for(int i = 1; i < n; i++){
            for(int j = 1; j < m; j++){
                if(ls[i][j] == 0)
                    continue;

                if(ls[i - 1][j] == 1 || ls[i][j - 1] == 1)
                    ls[i][j] = 1;
                else
                    ls[i][j] = 0;
            }
        }

        if(ls[n-1][m-1] == 1){
            cout << "YES" << endl;
            cout << n + m - 2 << endl;
        }

        else {
            cout << "NO" << endl;
        }
    }
}
