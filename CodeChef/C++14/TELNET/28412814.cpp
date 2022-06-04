#include <bits/stdc++.h>
using namespace std;

typedef long long int ll;

int main(){
    ios::sync_with_stdio(false);

    ll t; cin >> t;

    while(t--){
        int n, k; cin >> n >> k;

        vector<vector<pair<int, int>>> b(k);

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                int c; cin >> c; --c;

                pair<int, int> abc = make_pair(i, j);

                b[c].push_back(abc);
            }
        }

        vector<int> ans[k];

        for(int i = 0; i < b[0].size(); i++){
            ans[0].push_back(0);
        }

        for(int c = 1; c < k; c++){
            for(int i = 0; i < b[c].size(); i++){
                ans[c].push_back(INT_MAX);

                for(int j = 0; j < b[c - 1].size(); j++)
                    ans[c][i] = min(ans[c][i], ans[c-1][j] + abs(b[c][i].first - b[c-1][j].first) + abs(b[c][i].second - b[c-1][j].second));

            }
        }

        cout << *min_element(ans[k-1].begin(), ans[k-1].end()) << endl;
    }
}
