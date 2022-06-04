#include <iostream>
using namespace std;

typedef long long int ll;

int main(){
    ios::sync_with_stdio(false);

    ll t; cin >> t;

    while(t--){
        int n; cin >> n;

        int a[100000];

        int s = 0;

        for(int i = 0; i < n; i++){
            cin >> a[i];
            s += a[i];
        }

        int q; cin >> q;

        int i = 0, cnt = 0, last = -1;

        while(true){
            a[i + n] = s / n;

            if(s / n == last){
                cnt++;

                if(cnt == n)
                    break;
            }

            else
                cnt = 0;

            last = s / n;

            s += a[i + n] - a[i];

            i++;
        }

        n += i;

        for(int i = 0; i < q; i++){
            int x; cin >> x; x--;

            if(x < n) cout << a[x];
            else cout << last;

            cout << '\n';
        }
    }
}
