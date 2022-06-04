#include <bits/stdc++.h>
using namespace std;

#define int long long
#define endl '\n'

signed main() {
    ios::sync_with_stdio(false); cin.tie(NULL);

    int tcs; cin >> tcs;

    while (tcs--) {
        int n, q; cin >> n >> q;

        // ind stores a unique value for each range
        unordered_map<int, vector<int>> ind;

        // Unique value for each range
        int unique_val = 1;

        while (q--) {
            int l, r; cin >> l >> r;

            // Converting to 0-based indexing
            l--;
            r--;

            // Positive denotes beginning
            ind[l].push_back(unique_val);

            // Negative denotes ending
            // We use r+1 because r is inclusive in the range
            ind[r+1].push_back(-unique_val);

            // Next value to make it unique
            unique_val++;
        }

        int no_sts = 0;  // Number of statues that will be destroyed
        int ispeed = 0;  // Speed at which the number of statues destroyed increases

        // First occurrence of a range (stores l value of a range)
        unordered_map<int, int> occ;

        for (int i = 0; i < n; i++) {
            // For each "endpoint" (which is l or r+1)
            for (auto j : ind[i]) {

                // If it's a new range the speed with which the number of statues is destroyed will increase
                if (j > 0) {
                    occ[j] = i;
                    ispeed++;
                }

                // If it's the end of a range
                // The speed with which the number of statues is destroyed will decrease

                // The current amount of statues which are being destroyed at each index will decrease by how much it has contributed
                // Which is equal to r - l + 1, but since we set the endpoint to r+1, we should make it r - l
                // Here, (r = i) and (l = [first occurrence of -j] = occ[-j])
                else if (j < 0) {
                    ispeed--;
                    no_sts -= i - occ[-j];
                }
            }

            // The amount of statues destroyed at each index increases by the speed
            no_sts += ispeed;

            cout << no_sts << " ";
        }

        cout << endl;
    }
}
