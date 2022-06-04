#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
#define int long long

signed main(){
    int t; cin >> t;

    while(t--){
        int n, z; cin >> n >> z;

        priority_queue<int> que;

        for(int i = 0; i < n; i++){
            int x; cin >> x;
            que.push(x);
        }

        int cnt = 0;
        bool flag = false;

        while(z > 0){
            int x = que.top();
            que.pop();

            if(x == 0){
                flag = true;
                break;
            }

            cnt++;

            z -= x;
            que.push(x / 2);
        }

        if(flag)
            cout << "Evacuate" << endl;
        else
            cout << cnt << endl;
    }
}
