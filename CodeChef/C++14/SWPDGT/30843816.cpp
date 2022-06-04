#include <bits/stdc++.h>
using namespace std;

#define int long long

#define endl '\n'
#define speed ios_base::sync_with_stdio(false); cin.tie(NULL);

int get_int(vector<int> x){
    int cur = 0;

    for(int i = x.size() - 1; i >= 0; i--)
        cur = cur * 10 + x[i];

    return cur;
}

signed main(){
    speed;

    int t; cin >> t;

    while(t--){
        int a, b; cin >> a >> b;

        int maxi = a + b;

        vector<int> av;

        while(a != 0){
            av.push_back(a % 10);
            a /= 10;
        }

        vector<int> bv;

        while(b != 0){
            bv.push_back(b % 10);
            b /= 10;
        }

        for(int i = 0; i < av.size(); i++){
            for(int j = 0; j < bv.size(); j++){
                swap(av[i], bv[j]);
                maxi = max(maxi, get_int(av) + get_int(bv));
                swap(av[i], bv[j]);
            }
        }

        cout << maxi << endl;
    }

    return 0;
}
