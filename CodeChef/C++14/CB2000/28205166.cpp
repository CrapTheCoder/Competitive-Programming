#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while(t--){
        string a; cin >> a;
        int l = a.size();

        unordered_set<char> x;

        bool f = false;

        for(int i = 0; i < l; i++){
            if(x.find(a[i]) == x.end())
                x.insert(a[i]);
            else
                {cout << 0 << endl; f = true; break;}
        }

        if(f)
            continue;

        long int s = 1;

        for(int i = 0; i < l; i++){
            for(int j = i + 1; j < l; j++){
                s = (s * abs((a[i] - 48) - (a[j] - 48))) % MOD;
            }
        }

        cout << s << endl;
    }
}
