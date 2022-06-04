#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define speed ios::sync_with_stdio(false); cin.tie(NULL);

#define int long long

signed main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n, k; cin >> n >> k;
        unordered_map<int, int> last_occurrence;

        for(int i = 1; i <= k; i++)
            last_occurrence[i] = -1;

        int maxi = 0;

        for(int i = 0; i < n; i++){
            int x; cin >> x;

            // You can include all elements before the current flavor and after the previous occurrence of the last flavor
            // If last_occurrence[x] == -1, it'll be negated. i - (-1) - 1 = i + 1 - 1 = i, which makes sense
            maxi = max(maxi, i - last_occurrence[x] - 1);

            last_occurrence[x] = i;
        }

        for(int i = 1; i <= k; i++)
            // You can include all elements after the final occurrence of any flavor
            maxi = max(maxi, n - last_occurrence[i] - 1);

        cout << maxi << endl;
    }
}
