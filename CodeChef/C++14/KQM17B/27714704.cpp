#include <iostream>
using namespace std;

int dp[7][7];
char a[7][7];

void init(){
    for(int i = 0; i < 7; i++){
        for(int j = 0; j < 7; j++)
            dp[i][j] = 0;
    }
}

void track(int i, int j, int n, int m, int &c){
    if(dp[i][j] == 1 || a[i][j] == '#')
        return ;
    if(a[i][j] == 'K')
        c -= 1;

    dp[i][j] = 1;

    if(i + 1 < n) track(i + 1, j, n, m, c);
    if(j + 1 < m) track(i, j + 1, n, m, c);
    if(i - 1 >= 0) track(i - 1, j, n, m, c);
    if(j - 1 >= 0) track(i, j - 1, n, m, c);
}

int main()
{
    init();
    int n, m; cin >> n >> m;

    for(int i = 0; i < n; i++)
        cin >> a[i];

    int c = 0;
    int x, y;

    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(a[i][j] == 'X'){
                x = i;
                y = j;
            }

            if(a[i][j] == 'K')
                c++;
        }
    }

    track(x, y, n, m, c);

    if(c == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
}
