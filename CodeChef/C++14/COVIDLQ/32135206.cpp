#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int t; cin >> t;

    while(t--){
        int n; cin >> n;
        int a[n];

        for(int i = 0; i < n; i++)
            cin >> a[i];

        int last_person = -1;

        bool flag = true;

        for(int i = 0; i < n; i++){
            if(a[i] == 1){
                if((last_person != -1) && (i - last_person < 6)){
                    flag = false;
                    break;
                }

                last_person = i;
            }
        }

        if(flag)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}
