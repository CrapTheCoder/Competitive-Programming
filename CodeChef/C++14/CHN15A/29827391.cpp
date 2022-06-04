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
        int n, k; cin >> n >> k;
        int c = 0;
        
        for(int i = 0; i < n; i++){
            int x; cin >> x;
            
            x += k;
            
            if(x % 7 == 0)
                c++;
        }
        
        cout << c << endl;
    }
}
