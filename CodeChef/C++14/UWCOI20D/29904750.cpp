#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define speed ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

vector<pair<int, int>> v;

int main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n; cin >> n;

        char a[n][n];

        int f = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                cin >> a[i][j];

                if(a[i][j] == '1'){
                    if(i == j)
                        f++;

                    v.push_back({i, j});
                }
            }
        }

        if(f == n){
            cout << n * (n + 1) / 2 << endl;
            v.clear();
            continue;
        }

        int l = v.size();

        int c = 0;

        for(int i = 0; i < l; i++){
            int rmini = 0;
            int rmaxi = 0;

            int cmini = 0;
            int cmaxi = 0;

            for(int j = i; j < l; j++){
                if(v[j].first - v[i].first < rmini) rmini = v[j].first - v[i].first;
                if(v[j].first - v[i].first > rmaxi) rmaxi = v[j].first - v[i].first;

                if(v[j].second - v[i].second < cmini) cmini = v[j].second - v[i].second;
                if(v[j].second - v[i].second > cmaxi) cmaxi = v[j].second - v[i].second;

                // cout << i << " " << j << " " << j - i << " " << rmini << " " << rmaxi << " " << cmini << " " << cmaxi;

                if(abs(rmaxi - rmini) <= j - i && abs(cmaxi - cmini) <= j - i){
                    c++;
                    // cout << " YES";
                }

                cout << endl;
            }
        }

        cout << c << endl;

        v.clear();
    }
}
