#include <bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;


#define int long long
#define endl '\n'
#define all(iter) (iter).begin(), (iter).end()
#define rall(iter) (iter).rbegin(), (iter).rend()

const int MOD = 1e9 + 7;
const int INF = LLONG_MAX >> 1;

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tc; cin >> tc;
    while (tc--) {
        string s; cin >> s;
        int n = s.size();

        pair<char, int> c[n];
        for (int i = 0; i < n; i++)
            c[i] = {s[i], i};
        
        sort(c, c+n);

        vector<int> ind;
        
        ordered_set lst;
        for (int i = 0; i < n; i++)
            lst.insert(i);

        int lr = 0;

        for (int i = 0; i < n; i++) {
            int last_ind = ind.size() - 1;
            int first_lst = *lst.find_by_order(0);

            if (ind.empty() || (c[i].second > ind[last_ind] && s[first_lst] > c[i].first)) {
                ind.push_back(c[i].second);
                lst.erase(c[i].second);

                continue;
            }

            if (c[i].second > ind[last_ind] && s[first_lst] == c[i].first) {
                while (lr < lst.size() && s[*lst.find_by_order(lr)] == s[first_lst])
                    lr++;
                
                if (lr < lst.size() && s[first_lst] < s[*lst.find_by_order(lr)]) {
                    ind.push_back(c[i].second);
                    lst.erase(c[i].second);
                    lr--;
                }
            }
        }

        string sub, rst;
        set<int> inds(ind.begin(), ind.end());

        for (int i = 0; i < n; i++)
            inds.count(i) ? (sub += s[i]) : (rst += s[i]);
        
        cout << sub + rst << endl;
    }
}
