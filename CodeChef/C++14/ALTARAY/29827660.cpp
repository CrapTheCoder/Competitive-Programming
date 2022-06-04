#include <bits/stdc++.h>

using namespace std;

typedef int integer;
typedef long long int ll;

#define int ll
#define endl '\n'

#define speed ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

integer main(){
    speed;

    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        int a[n];

        for(int i = 0; i < n; i++)
            cin >> a[i];

        int p[n];

        for(int i = 0; i < n; i++){
            int c = 1;

            if(i == 0 || p[i-1] == 1){
                int j = i + 1;

                while(j < n && a[j] < 0 != a[j-1] < 0){
                    c++; j++;
                }

                p[i] = c;
            }

            else {
                p[i] = p[i-1] - 1;
            }
        }

        for(int i = 0; i < n; i++)
            cout << p[i] << " ";

        cout << endl;
    }
}
