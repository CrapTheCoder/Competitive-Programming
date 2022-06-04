#include <vector>
#include <utility>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t; cin >> t;

    while(t--){
        int n, m, k; cin >> n >> m >> k;
        int a = 0;

        unordered_map<int, unordered_set<int>> rs;
        unordered_map<int, unordered_set<int>> cs;
        vector<pair<int, int>> rcs;

        for(int i = 0; i < k; i++){
            int r, c; cin >> r >> c;
            r--; c--;

            rs[r].insert(c);
            cs[c].insert(r);

            rcs.push_back(make_pair(r, c));
        }

        for(int i = 0; i < k; i++){
            int r = rcs[i].first;
            int c = rcs[i].second;

            if(rs[r].find(c-1) == rs[r].end()) a++;
            if(rs[r].find(c+1) == rs[r].end()) a++;
            if(cs[c].find(r-1) == cs[c].end()) a++;
            if(cs[c].find(r+1) == cs[c].end()) a++;
        }

        cout << a << endl;
    }
}
